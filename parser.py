import pyparsing as pp


identifier = pp.Word(pp.alphanums+'_')

variable = pp.Word(pp.alphanums.upper(), bodyChars=pp.alphanums+'_')

functor = pp.Word(pp.alphanums.lower()+'_') ^ '\'' + pp.Word(pp.alphanums.lower()+'_') + '\''
binary_connective = pp.Literal('|') | pp.Literal('&') | pp.Literal('<=>') \
                    | pp.Literal('=>') | pp.Literal('<=') | pp.Literal('<~>') \
                    | pp.Literal('~&') | pp.Literal('~|') | pp.Literal('!=') | pp.Literal('=')

unary_connective = pp.Literal('~')

fof_formula = pp.Forward()
fof_plain_term = pp.Forward()
fof_term = pp.Forward()
fof_atomic_formula = ('$' + fof_plain_term) ^ fof_plain_term ^ fof_term + '=' + fof_term
fof_function_term = ('$' + fof_plain_term) ^ fof_plain_term
fof_term << (fof_function_term ^ variable)
term_list = pp.delimitedList(fof_term, delim=',')
fof_plain_term << (functor ^ \
                  (functor + '(' + term_list + ')').setParseAction(lambda x: dict(type:'function')))
fof_unitary_formula = pp.Forward()
fof_unary_formula = (unary_connective + fof_unitary_formula)
fof_quantifier = pp.Literal('!') ^ pp.Literal('?')
fof_quantified_formula = fof_quantifier + '[' + pp.delimitedList(variable, delim=',') + ']' + ':' + fof_unitary_formula
fof_unitary_formula << (fof_quantified_formula ^ (unary_connective + fof_unitary_formula) ^ fof_atomic_formula | '(' + fof_formula + ')')
fof_binary_formula = fof_unitary_formula + binary_connective + fof_unitary_formula
fof_formula << (fof_binary_formula ^ fof_unary_formula ^ fof_unitary_formula)

cnf_formula = pp.Forward()
disjunction = '(' + pp.delimitedList(cnf_formula, delim='|') + ')'
literal = ('~' + fof_atomic_formula).setParseAction(lambda x: dict(type='negation', expression=x[1])) ^ fof_atomic_formula.setParseAction(lambda x: dict(type='negation', expression=x[0]))
#cnf_conjunction = '(' + pp.delimitedList(cnf_formula, delim='|') + ')'
cnf_formula << (literal ^ disjunction)


cnf_triple = (pp.Suppress('cnf(') + identifier + pp.Suppress(',') + identifier
              + pp.Suppress(',') + cnf_formula + pp.Suppress(').')
              ).setParseAction(lambda x: dict(name=x[0], type=x[1], value=x[2]))
fof_triple = 'fof(' + identifier + ',' + identifier + ',' + fof_formula + ').'
#tff_triple = 'tff(' + pp.Word(pp.alphanums) + ',' + pp.Word(pp.alphanums) + ',' + tff_formula + + ').'
#thf_triple = 'thf(' + pp.Word(pp.alphanums) + ',' + pp.Word(pp.alphanums) + ',' + thf_formula + + ').'

comment = '%' + pp.restOfLine()

tptp_input = comment ^ cnf_triple ^ fof_triple # ^ tff_triple ^ thf_triple



tptp_file = pp.OneOrMore(tptp_input)
t = 'a = b' #"apply_to_two_arguments(Xf,apply_to_two_arguments(Xf,X,Y),Z) = apply_to_two_arguments(Xf,X,apply_to_two_arguments(Xf,Y,Z))"
s = """cnf(associative_system1,axiom,
    ( ~ associative(Xs,Xf)
    | ~ member(X,Xs)
    | ~ member(Y,Xs)
    | ~ member(Z,Xs)
    | apply_to_two_arguments(Xf,apply_to_two_arguments(Xf,X,Y),Z) = apply_to_two_arguments(Xf,X,apply_to_two_arguments(Xf,Y,Z)) ))."""

print( cnf_triple.parseString(s, True))
#print(tptp_file.parseFile('data/TPTP-v7.1.0/Axioms/ALG001-0.ax',True))