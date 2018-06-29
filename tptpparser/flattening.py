# Generated from tptp_v7_0_0_0.g4 by ANTLR 4.5.1
from antlr4 import *
import tptpparser.structures as structures
from parser.tptp_v7_0_0_0Parser import tptp_v7_0_0_0Parser
from parser.tptp_v7_0_0_0Visitor import tptp_v7_0_0_0Visitor

# This class defines a complete generic visitor for a parse tree produced by tptp_v7_0_0_0Parser.

class FOFFlatteningVisitor(tptp_v7_0_0_0Visitor):

    def visitTerminal(self, node):
        return node.symbol.text

    def visit_first(self, ctx):
        assert len(ctx.children) == 1
        return self.visit(ctx.children[0])

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tptp_file.
    def visitTptp_file(self, ctx:tptp_v7_0_0_0Parser.Tptp_fileContext):
        return [self.visit(c) for c in ctx.children[:-1]]


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tptp_input.
    def visitTptp_input(self, ctx:tptp_v7_0_0_0Parser.Tptp_inputContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#annotated_formula.
    def visitAnnotated_formula(self, ctx:tptp_v7_0_0_0Parser.Annotated_formulaContext):
        annotated = ctx.children[0]
        return structures.AnnotatedFormula(
            self.visit(annotated.children[1]),  # name
            self.visit(annotated.children[3]),  # role
            self.visit(annotated.children[5]))  # formula


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tpi_formula.
    def visitTpi_formula(self, ctx:tptp_v7_0_0_0Parser.Tpi_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#annotations.
    def visitAnnotations(self, ctx:tptp_v7_0_0_0Parser.AnnotationsContext):
        return self.visitChildren(ctx)

    _ROLE_MAP = {
        'axiom': structures.FormulaRole.AXIOM,
        'hypothesis': structures.FormulaRole.HYPOTHESIS,
        'definition': structures.FormulaRole.DEFINITION,
        'assumption': structures.FormulaRole.ASSUMPTION,
        'lemma': structures.FormulaRole.LEMMA,
        'theorem': structures.FormulaRole.THEOREM,
        'corollary': structures.FormulaRole.COROLLARY,
        'conjecture': structures.FormulaRole.CONJECTURE,
        'negated_conjecture': structures.FormulaRole.NEGATED_CONJECTURE,
        'plain': structures.FormulaRole.PLAIN,
        'type': structures.FormulaRole.TYPE,
        'fi_domain': structures.FormulaRole.FI_DOMAIN,
        'fi_functors': structures.FormulaRole.FI_FUNCTORS,
        'fi_predicates': structures.FormulaRole.FI_PREDICATES,
        'unknown': structures.FormulaRole.UNKNOWN,
    }

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#formula_role.
    def visitFormula_role(self, ctx:tptp_v7_0_0_0Parser.Formula_roleContext):
        return self._ROLE_MAP[self.visit_first(ctx)]


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_formula.
    def visitThf_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_logic_formula.
    def visitThf_logic_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_logic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_binary_formula.
    def visitThf_binary_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_binary_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_binary_pair.
    def visitThf_binary_pair(self, ctx:tptp_v7_0_0_0Parser.Thf_binary_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_binary_tuple.
    def visitThf_binary_tuple(self, ctx:tptp_v7_0_0_0Parser.Thf_binary_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_or_formula.
    def visitThf_or_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_or_formulaContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.DISJUNCTION,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_and_formula.
    def visitThf_and_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_and_formulaContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.CONJUNCTION,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_apply_formula.
    def visitThf_apply_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_apply_formulaContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.APPLY,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_unitary_formula.
    def visitThf_unitary_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_unitary_formulaContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        if len(ctx.children) == 3:
            return self.visit(ctx.children[1])
        raise NotImplementedError

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_quantified_formula.
    def visitThf_quantified_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_quantified_formulaContext):
        return structures.QuantifiedFormula(
            self.visit(ctx.children[0].children[0]),
            self.visit(ctx.children[0].children[2]),
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_quantification.
    def visitThf_quantification(self, ctx:tptp_v7_0_0_0Parser.Thf_quantificationContext):
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_variable_list.
    def visitThf_variable_list(self, ctx:tptp_v7_0_0_0Parser.Thf_variable_listContext):
        if len(ctx.children) == 1:
            return [self.visit_first(ctx)]
        if len(ctx.children) == 3:
            return self.visit(ctx.children[2]).append(ctx.children[0])
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_variable.
    def visitThf_variable(self, ctx:tptp_v7_0_0_0Parser.Thf_variableContext):
        return self.visitVariable(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_typed_variable.
    def visitThf_typed_variable(self, ctx:tptp_v7_0_0_0Parser.Thf_typed_variableContext):
        return structures.TypedVariable(
            self.visit(ctx.children[0]),
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_unary_formula.
    def visitThf_unary_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_unary_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_atom.
    def visitThf_atom(self, ctx:tptp_v7_0_0_0Parser.Thf_atomContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_function.
    def visitThf_function(self, ctx:tptp_v7_0_0_0Parser.Thf_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_conn_term.
    def visitThf_conn_term(self, ctx:tptp_v7_0_0_0Parser.Thf_conn_termContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_conditional.
    def visitThf_conditional(self, ctx:tptp_v7_0_0_0Parser.Thf_conditionalContext):
        return structures.Conditional(
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3]),
            self.visit(ctx.children[5]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_let.
    def visitThf_let(self, ctx:tptp_v7_0_0_0Parser.Thf_letContext):
        return structures.Let(
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3]),
            self.visit(ctx.children[5]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_arguments.
    def visitThf_arguments(self, ctx:tptp_v7_0_0_0Parser.Thf_argumentsContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_type_formula.
    def visitThf_type_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_type_formulaContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[1])
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_typeable_formula.
    def visitThf_typeable_formula(self, ctx:tptp_v7_0_0_0Parser.Thf_typeable_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_subtype.
    def visitThf_subtype(self, ctx:tptp_v7_0_0_0Parser.Thf_subtypeContext):
        return structures.Subtype(
            self.visit(ctx.children[0]),
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_top_level_type.
    def visitThf_top_level_type(self, ctx:tptp_v7_0_0_0Parser.Thf_top_level_typeContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_unitary_type.
    def visitThf_unitary_type(self, ctx:tptp_v7_0_0_0Parser.Thf_unitary_typeContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_apply_type.
    def visitThf_apply_type(self, ctx:tptp_v7_0_0_0Parser.Thf_apply_typeContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_binary_type.
    def visitThf_binary_type(self, ctx:tptp_v7_0_0_0Parser.Thf_binary_typeContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_mapping_type.
    def visitThf_mapping_type(self, ctx:tptp_v7_0_0_0Parser.Thf_mapping_typeContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.MAPPING,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_xprod_type.
    def visitThf_xprod_type(self, ctx:tptp_v7_0_0_0Parser.Thf_xprod_typeContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.PRODUCT,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_union_type.
    def visitThf_union_type(self, ctx:tptp_v7_0_0_0Parser.Thf_union_typeContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.UNION,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_sequent.
    def visitThf_sequent(self, ctx:tptp_v7_0_0_0Parser.Thf_sequentContext):
        if isinstance(ctx.children[0], tptp_v7_0_0_0Parser.Thf_tupleContext):
            return structures.BinaryFormula(
                self.visit(ctx.children[0]),
                structures.BinaryConnective.GENTZEN_ARROW,
                self.visit(ctx.children[2]))
        else:
            return self.visit(ctx.children[1])


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_tuple.
    def visitThf_tuple(self, ctx:tptp_v7_0_0_0Parser.Thf_tupleContext):
        if len(ctx.children) == 1:
            return []
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[1])
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_formula_list.
    def visitThf_formula_list(self, ctx:tptp_v7_0_0_0Parser.Thf_formula_listContext):
        if len(ctx.children) == 1:
            return [self.visit_first(ctx)]
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[2]).append(self.visit(ctx.children[0]))
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tfx_formula.
    def visitTfx_formula(self, ctx:tptp_v7_0_0_0Parser.Tfx_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tfx_logic_formula.
    def visitTfx_logic_formula(self, ctx:tptp_v7_0_0_0Parser.Tfx_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_formula.
    def visitTff_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_logic_formula.
    def visitTff_logic_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_logic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_binary_formula.
    def visitTff_binary_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_binary_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_binary_nonassoc.
    def visitTff_binary_nonassoc(self, ctx:tptp_v7_0_0_0Parser.Tff_binary_nonassocContext):
        return self.visitFof_binary_nonassoc(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_binary_assoc.
    def visitTff_binary_assoc(self, ctx:tptp_v7_0_0_0Parser.Tff_binary_assocContext):
        return self.visitFof_binary_assoc(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_or_formula.
    def visitTff_or_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_or_formulaContext):
        return self.visitFof_or_formula(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_and_formula.
    def visitTff_and_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_and_formulaContext):
        return self.visitFof_and_formula(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_unitary_formula.
    def visitTff_unitary_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_unitary_formulaContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[1])
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_quantified_formula.
    def visitTff_quantified_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_quantified_formulaContext):
        return self.visitFof_quantified_formula(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_variable_list.
    def visitTff_variable_list(self, ctx:tptp_v7_0_0_0Parser.Tff_variable_listContext):
        return self.visitFof_variable_list(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_variable.
    def visitTff_variable(self, ctx:tptp_v7_0_0_0Parser.Tff_variableContext):
        return self.visitThf_variable(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_typed_variable.
    def visitTff_typed_variable(self, ctx:tptp_v7_0_0_0Parser.Tff_typed_variableContext):
        return self.visitThf_typed_variable(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_unary_formula.
    def visitTff_unary_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_unary_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_atomic_formula.
    def visitTff_atomic_formula(self, ctx:tptp_v7_0_0_0Parser.Tff_atomic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_conditional.
    def visitTff_conditional(self, ctx:tptp_v7_0_0_0Parser.Tff_conditionalContext):
        return self.visitThf_conditional(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let.
    def visitTff_let(self, ctx:tptp_v7_0_0_0Parser.Tff_letContext):
        return self.visitThf_let(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_term_defns.
    def visitTff_let_term_defns(self, ctx:tptp_v7_0_0_0Parser.Tff_let_term_defnsContext):
        if len(ctx.children) == 1:
            return [self.visit_first(ctx)]
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[1])
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_term_list.
    def visitTff_let_term_list(self, ctx:tptp_v7_0_0_0Parser.Tff_let_term_listContext):
        if len(ctx.children) == 1:
            return [self.visit_first(ctx)]
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[2]).append(self.visit(ctx.children[0]))
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_term_defn.
    def visitTff_let_term_defn(self, ctx:tptp_v7_0_0_0Parser.Tff_let_term_defnContext):
        return structures.BinaryFormula(
                self.visit(ctx.children[0]),
                structures.BinaryConnective.ASSIGN,
                self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_term_binding.
    def visitTff_let_term_binding(self, ctx:tptp_v7_0_0_0Parser.Tff_let_term_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_formula_defns.
    def visitTff_let_formula_defns(self, ctx:tptp_v7_0_0_0Parser.Tff_let_formula_defnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_formula_list.
    def visitTff_let_formula_list(self, ctx:tptp_v7_0_0_0Parser.Tff_let_formula_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_formula_defn.
    def visitTff_let_formula_defn(self, ctx:tptp_v7_0_0_0Parser.Tff_let_formula_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_formula_binding.
    def visitTff_let_formula_binding(self, ctx:tptp_v7_0_0_0Parser.Tff_let_formula_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_sequent.
    def visitTff_sequent(self, ctx:tptp_v7_0_0_0Parser.Tff_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_formula_tuple.
    def visitTff_formula_tuple(self, ctx:tptp_v7_0_0_0Parser.Tff_formula_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_formula_tuple_list.
    def visitTff_formula_tuple_list(self, ctx:tptp_v7_0_0_0Parser.Tff_formula_tuple_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_typed_atom.
    def visitTff_typed_atom(self, ctx:tptp_v7_0_0_0Parser.Tff_typed_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_subtype.
    def visitTff_subtype(self, ctx:tptp_v7_0_0_0Parser.Tff_subtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_top_level_type.
    def visitTff_top_level_type(self, ctx:tptp_v7_0_0_0Parser.Tff_top_level_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tf1_quantified_type.
    def visitTf1_quantified_type(self, ctx:tptp_v7_0_0_0Parser.Tf1_quantified_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_monotype.
    def visitTff_monotype(self, ctx:tptp_v7_0_0_0Parser.Tff_monotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_unitary_type.
    def visitTff_unitary_type(self, ctx:tptp_v7_0_0_0Parser.Tff_unitary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_atomic_type.
    def visitTff_atomic_type(self, ctx:tptp_v7_0_0_0Parser.Tff_atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_type_arguments.
    def visitTff_type_arguments(self, ctx:tptp_v7_0_0_0Parser.Tff_type_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_mapping_type.
    def visitTff_mapping_type(self, ctx:tptp_v7_0_0_0Parser.Tff_mapping_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_xprod_type.
    def visitTff_xprod_type(self, ctx:tptp_v7_0_0_0Parser.Tff_xprod_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tcf_formula.
    def visitTcf_formula(self, ctx:tptp_v7_0_0_0Parser.Tcf_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tcf_logic_formula.
    def visitTcf_logic_formula(self, ctx:tptp_v7_0_0_0Parser.Tcf_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tcf_quantified_formula.
    def visitTcf_quantified_formula(self, ctx:tptp_v7_0_0_0Parser.Tcf_quantified_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_formula.
    def visitFof_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_logic_formula.
    def visitFof_logic_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_logic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_binary_formula.
    def visitFof_binary_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_binary_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_binary_nonassoc.
    def visitFof_binary_nonassoc(self, ctx:tptp_v7_0_0_0Parser.Fof_binary_nonassocContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            self.visit(ctx.children[1]),
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_binary_assoc.
    def visitFof_binary_assoc(self, ctx:tptp_v7_0_0_0Parser.Fof_binary_assocContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_or_formula.
    def visitFof_or_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_or_formulaContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.DISJUNCTION,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_and_formula.
    def visitFof_and_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_and_formulaContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.CONJUNCTION,
            self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_unitary_formula.
    def visitFof_unitary_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_unitary_formulaContext):
        if len(ctx.children) == 1:
            # case: <fof_quantified_formula> | <fof_atomic_formula>
            return self.visit_first(ctx)
        else:
            # case: (<fof_logic_formula>)
            return self.visit(ctx.children[1])


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_quantified_formula.
    def visitFof_quantified_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_quantified_formulaContext):
        return structures.QuantifiedFormula(
            self.visit(ctx.children[0]),  # quantifier
            self.visit(ctx.children[2]),  # variable list
            self.visit(ctx.children[5]),  # formula
        )


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_variable_list.
    def visitFof_variable_list(self, ctx:tptp_v7_0_0_0Parser.Fof_variable_listContext):
        return [self.visit(ctx.children[i])
                for i in range(0, len(ctx.children), 2)]


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_unary_formula.
    def visitFof_unary_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_unary_formulaContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        elif len(ctx.children) == 2:
            return structures.UnaryFormula(
                self.visit(ctx.children[0]),
                self.visit(ctx.children[1])
            )
        raise NotImplementedError

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_infix_unary.
    def visitFof_infix_unary(self, ctx:tptp_v7_0_0_0Parser.Fof_infix_unaryContext):
        return structures.BinaryFormula(
            self.visit(ctx.children[0]),
            structures.BinaryConnective.NEQ,
            self.visit(ctx.children[2]))



    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_atomic_formula.
    def visitFof_atomic_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_atomic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_plain_atomic_formula.
    def visitFof_plain_atomic_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_plain_atomic_formulaContext):
        if len(ctx.children) == 1:
            # case: <proposition>
            return self.visit_first(ctx)
        else:
            # case: <predicate>(<fof_arguments>)
            return structures.PredicateExpression(
                self.visit(ctx.children[0]),
                self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_atomic_formula.
    def visitFof_defined_atomic_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_atomic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_plain_formula.
    def visitFof_defined_plain_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_plain_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_infix_formula.
    def visitFof_defined_infix_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_infix_formulaContext):
        return structures.BinaryFormula(
                self.visit(ctx.children[0]),
                structures.BinaryConnective.EQ,
                self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_system_atomic_formula.
    def visitFof_system_atomic_formula(self, ctx:tptp_v7_0_0_0Parser.Fof_system_atomic_formulaContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_plain_term.
    def visitFof_plain_term(self, ctx:tptp_v7_0_0_0Parser.Fof_plain_termContext):
        if len(ctx.children) == 1:
            # case: <constant>
            return self.visit_first(ctx)
        else:
            # case: <functor>(<fof_arguments>)
            return structures.FunctorExpression(
                self.visit(ctx.children[0]),
                self.visit(ctx.children[2]))


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_term.
    def visitFof_defined_term(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_atomic_term.
    def visitFof_defined_atomic_term(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_atomic_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_defined_plain_term.
    def visitFof_defined_plain_term(self, ctx:tptp_v7_0_0_0Parser.Fof_defined_plain_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_system_term.
    def visitFof_system_term(self, ctx:tptp_v7_0_0_0Parser.Fof_system_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_arguments.
    def visitFof_arguments(self, ctx:tptp_v7_0_0_0Parser.Fof_argumentsContext):
        return [self.visit(ctx.children[i])
                for i in range(0, len(ctx.children), 2)]

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_term.
    def visitFof_term(self, ctx:tptp_v7_0_0_0Parser.Fof_termContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_function_term.
    def visitFof_function_term(self, ctx:tptp_v7_0_0_0Parser.Fof_function_termContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_conditional_term.
    def visitTff_conditional_term(self, ctx:tptp_v7_0_0_0Parser.Tff_conditional_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_let_term.
    def visitTff_let_term(self, ctx:tptp_v7_0_0_0Parser.Tff_let_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_tuple_term.
    def visitTff_tuple_term(self, ctx:tptp_v7_0_0_0Parser.Tff_tuple_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_sequent.
    def visitFof_sequent(self, ctx:tptp_v7_0_0_0Parser.Fof_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_formula_tuple.
    def visitFof_formula_tuple(self, ctx:tptp_v7_0_0_0Parser.Fof_formula_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_formula_tuple_list.
    def visitFof_formula_tuple_list(self, ctx:tptp_v7_0_0_0Parser.Fof_formula_tuple_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#cnf_formula.
    def visitCnf_formula(self, ctx:tptp_v7_0_0_0Parser.Cnf_formulaContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        elif len(ctx.children) == 3:
            return self.visit(ctx.children[1])


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#cnf_disjunction.
    def visitCnf_disjunction(self, ctx:tptp_v7_0_0_0Parser.Cnf_disjunctionContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        elif len(ctx.children) == 3:
            return structures.BinaryFormula(
                self.visit(ctx.children[0]),
                structures.BinaryConnective.DISJUNCTION,
                self.visit(ctx.children[2])
            )


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#cnf_literal.
    def visitCnf_literal(self, ctx:tptp_v7_0_0_0Parser.Cnf_literalContext):
        if len(ctx.children) == 1:
            return self.visit_first(ctx)
        else:
            return structures.UnaryFormula(
                structures.UnaryConnective.NEGATION,
                self.visit(ctx.children[1]),
            )


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_quantifier.
    def visitThf_quantifier(self, ctx:tptp_v7_0_0_0Parser.Thf_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#th0_quantifier.
    def visitTh0_quantifier(self, ctx:tptp_v7_0_0_0Parser.Th0_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#th1_quantifier.
    def visitTh1_quantifier(self, ctx:tptp_v7_0_0_0Parser.Th1_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_pair_connective.
    def visitThf_pair_connective(self, ctx:tptp_v7_0_0_0Parser.Thf_pair_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#thf_unary_connective.
    def visitThf_unary_connective(self, ctx:tptp_v7_0_0_0Parser.Thf_unary_connectiveContext):
        connective = self.visit(ctx)
        if connective == '~':
            return structures.UnaryConnective.NEGATION
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#th1_unary_connective.
    def visitTh1_unary_connective(self, ctx:tptp_v7_0_0_0Parser.Th1_unary_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#tff_pair_connective.
    def visitTff_pair_connective(self, ctx:tptp_v7_0_0_0Parser.Tff_pair_connectiveContext):
        return self.visitChildren(ctx)

    _QUANTIFIER_MAP = {
        '!': structures.Quantifier.UNIVERSAL,
        '?': structures.Quantifier.EXISTENTIAL
    }
    # Visit a parse tree produced by tptp_v7_0_0_0Parser#fof_quantifier.
    def visitFof_quantifier(self, ctx:tptp_v7_0_0_0Parser.Fof_quantifierContext):
        return self._QUANTIFIER_MAP[self.visit_first(ctx)]


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#binary_connective.
    def visitBinary_connective(self, ctx:tptp_v7_0_0_0Parser.Binary_connectiveContext):
        if len(ctx.children) == 1:
            connective = self.visit_first(ctx)
            if connective == '<=>':
                return structures.BinaryConnective.BIIMPLICATION
            elif connective == '=>':
                return structures.BinaryConnective.IMPLICATION
            elif connective == '<=':
                return structures.BinaryConnective.REVERSE_IMPLICATION
            elif connective == '<~>':
                return structures.BinaryConnective.SIMILARITY
            elif connective == '~&':
                return structures.BinaryConnective.NEGATED_CONJUNCTION
            elif connective == '~|':
                return structures.BinaryConnective.NEGATED_DISJUNCTION
        raise NotImplementedError(connective)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#assoc_connective.
    def visitAssoc_connective(self, ctx:tptp_v7_0_0_0Parser.Assoc_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#unary_connective.
    def visitUnary_connective(self, ctx:tptp_v7_0_0_0Parser.Unary_connectiveContext):
        connective = self.visit_first(ctx)
        if connective == '~':
            return structures.UnaryConnective.NEGATION
        raise NotImplementedError


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#type_constant.
    def visitType_constant(self, ctx:tptp_v7_0_0_0Parser.Type_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#type_functor.
    def visitType_functor(self, ctx:tptp_v7_0_0_0Parser.Type_functorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_type.
    def visitDefined_type(self, ctx:tptp_v7_0_0_0Parser.Defined_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#system_type.
    def visitSystem_type(self, ctx:tptp_v7_0_0_0Parser.System_typeContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#atom.
    def visitAtom(self, ctx:tptp_v7_0_0_0Parser.AtomContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#untyped_atom.
    def visitUntyped_atom(self, ctx:tptp_v7_0_0_0Parser.Untyped_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_proposition.
    def visitDefined_proposition(self, ctx:tptp_v7_0_0_0Parser.Defined_propositionContext):
        if isinstance(ctx.children[0], tptp_v7_0_0_0Parser.Defined_predicateContext):
            return self.visit_first(ctx)
        else:
            prop = self.visit_first(ctx)
            if prop == '$true':
                return True
            elif prop == '$false':
                return False
        raise NotImplementedError


    _DEFINED_PREDICATE_MAP = {
        '$distinct': structures.DefinedPredicate.DISTINCT,
        '$less': structures.DefinedPredicate.LESS,
        '$lesseq': structures.DefinedPredicate.LESS_EQ,
        '$greater': structures.DefinedPredicate.GREATER,
        '$greatereq': structures.DefinedPredicate.GREATER_EQ,
        '$is_int': structures.DefinedPredicate.IS_INT,
        '$is_rat': structures.DefinedPredicate.IS_RAT,
        '$box_P': structures.DefinedPredicate.BOX_P,
        '$box_i': structures.DefinedPredicate.BOX_I,
        '$box_int': structures.DefinedPredicate.BOX_INT,
        '$box': structures.DefinedPredicate.BOX,
        '$dia_P': structures.DefinedPredicate.DIA_P,
        '$dia_i': structures.DefinedPredicate.DIA_I,
        '$dia_int': structures.DefinedPredicate.DIA_INT,
        '$dia': structures.DefinedPredicate.DIA,
    }

    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_predicate.
    def visitDefined_predicate(self, ctx:tptp_v7_0_0_0Parser.Defined_predicateContext):
        if isinstance(ctx.children[0], tptp_v7_0_0_0Parser.Atomic_defined_wordContext):
            return self.visit_first(ctx)
        else:
            return self._DEFINED_PREDICATE_MAP[self.visit_first(ctx)]


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_infix_pred.
    def visitDefined_infix_pred(self, ctx:tptp_v7_0_0_0Parser.Defined_infix_predContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#constant.
    def visitConstant(self, ctx:tptp_v7_0_0_0Parser.ConstantContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#functor.
    def visitFunctor(self, ctx:tptp_v7_0_0_0Parser.FunctorContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#system_constant.
    def visitSystem_constant(self, ctx:tptp_v7_0_0_0Parser.System_constantContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#system_functor.
    def visitSystem_functor(self, ctx:tptp_v7_0_0_0Parser.System_functorContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_constant.
    def visitDefined_constant(self, ctx:tptp_v7_0_0_0Parser.Defined_constantContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_functor.
    def visitDefined_functor(self, ctx:tptp_v7_0_0_0Parser.Defined_functorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#defined_term.
    def visitDefined_term(self, ctx:tptp_v7_0_0_0Parser.Defined_termContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#variable.
    def visitVariable(self, ctx:tptp_v7_0_0_0Parser.VariableContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#source.
    def visitSource(self, ctx:tptp_v7_0_0_0Parser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#sources.
    def visitSources(self, ctx:tptp_v7_0_0_0Parser.SourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#dag_source.
    def visitDag_source(self, ctx:tptp_v7_0_0_0Parser.Dag_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_record.
    def visitInference_record(self, ctx:tptp_v7_0_0_0Parser.Inference_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_rule.
    def visitInference_rule(self, ctx:tptp_v7_0_0_0Parser.Inference_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_parents.
    def visitInference_parents(self, ctx:tptp_v7_0_0_0Parser.Inference_parentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#parent_list.
    def visitParent_list(self, ctx:tptp_v7_0_0_0Parser.Parent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#parent_info.
    def visitParent_info(self, ctx:tptp_v7_0_0_0Parser.Parent_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#parent_details.
    def visitParent_details(self, ctx:tptp_v7_0_0_0Parser.Parent_detailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#internal_source.
    def visitInternal_source(self, ctx:tptp_v7_0_0_0Parser.Internal_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#intro_type.
    def visitIntro_type(self, ctx:tptp_v7_0_0_0Parser.Intro_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#external_source.
    def visitExternal_source(self, ctx:tptp_v7_0_0_0Parser.External_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#file_source.
    def visitFile_source(self, ctx:tptp_v7_0_0_0Parser.File_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#file_info.
    def visitFile_info(self, ctx:tptp_v7_0_0_0Parser.File_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#theory.
    def visitTheory(self, ctx:tptp_v7_0_0_0Parser.TheoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#theory_name.
    def visitTheory_name(self, ctx:tptp_v7_0_0_0Parser.Theory_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#creator_source.
    def visitCreator_source(self, ctx:tptp_v7_0_0_0Parser.Creator_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#creator_name.
    def visitCreator_name(self, ctx:tptp_v7_0_0_0Parser.Creator_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#optional_info.
    def visitOptional_info(self, ctx:tptp_v7_0_0_0Parser.Optional_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#useful_info.
    def visitUseful_info(self, ctx:tptp_v7_0_0_0Parser.Useful_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#info_items.
    def visitInfo_items(self, ctx:tptp_v7_0_0_0Parser.Info_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#info_item.
    def visitInfo_item(self, ctx:tptp_v7_0_0_0Parser.Info_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#formula_item.
    def visitFormula_item(self, ctx:tptp_v7_0_0_0Parser.Formula_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#description_item.
    def visitDescription_item(self, ctx:tptp_v7_0_0_0Parser.Description_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#iquote_item.
    def visitIquote_item(self, ctx:tptp_v7_0_0_0Parser.Iquote_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_item.
    def visitInference_item(self, ctx:tptp_v7_0_0_0Parser.Inference_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_status.
    def visitInference_status(self, ctx:tptp_v7_0_0_0Parser.Inference_statusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#status_value.
    def visitStatus_value(self, ctx:tptp_v7_0_0_0Parser.Status_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#inference_info.
    def visitInference_info(self, ctx:tptp_v7_0_0_0Parser.Inference_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#assumptions_record.
    def visitAssumptions_record(self, ctx:tptp_v7_0_0_0Parser.Assumptions_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#refutation.
    def visitRefutation(self, ctx:tptp_v7_0_0_0Parser.RefutationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#new_symbol_record.
    def visitNew_symbol_record(self, ctx:tptp_v7_0_0_0Parser.New_symbol_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#new_symbol_list.
    def visitNew_symbol_list(self, ctx:tptp_v7_0_0_0Parser.New_symbol_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#principal_symbol.
    def visitPrincipal_symbol(self, ctx:tptp_v7_0_0_0Parser.Principal_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#include.
    def visitInclude(self, ctx:tptp_v7_0_0_0Parser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#formula_selection.
    def visitFormula_selection(self, ctx:tptp_v7_0_0_0Parser.Formula_selectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#name_list.
    def visitName_list(self, ctx:tptp_v7_0_0_0Parser.Name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#general_term.
    def visitGeneral_term(self, ctx:tptp_v7_0_0_0Parser.General_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#general_data.
    def visitGeneral_data(self, ctx:tptp_v7_0_0_0Parser.General_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#general_function.
    def visitGeneral_function(self, ctx:tptp_v7_0_0_0Parser.General_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#formula_data.
    def visitFormula_data(self, ctx:tptp_v7_0_0_0Parser.Formula_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#general_list.
    def visitGeneral_list(self, ctx:tptp_v7_0_0_0Parser.General_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#general_terms.
    def visitGeneral_terms(self, ctx:tptp_v7_0_0_0Parser.General_termsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#name.
    def visitName(self, ctx:tptp_v7_0_0_0Parser.NameContext):
        return self.visit(ctx.children[0])


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#atomic_word.
    def visitAtomic_word(self, ctx:tptp_v7_0_0_0Parser.Atomic_wordContext):
        return self.visit_first(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#atomic_defined_word.
    def visitAtomic_defined_word(self, ctx:tptp_v7_0_0_0Parser.Atomic_defined_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#atomic_system_word.
    def visitAtomic_system_word(self, ctx:tptp_v7_0_0_0Parser.Atomic_system_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#number.
    def visitNumber(self, ctx:tptp_v7_0_0_0Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptp_v7_0_0_0Parser#file_name.
    def visitFile_name(self, ctx:tptp_v7_0_0_0Parser.File_nameContext):
        return self.visitChildren(ctx)


    """def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return [nextResult]
        return aggregate.append(nextResult)"""
