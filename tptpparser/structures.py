from enum import Enum


class TPTPElement:
    pass


class Quantifier(Enum):
    UNIVERSAL = 0
    EXISTENTIAL = 1


class FormulaRole(Enum):
    AXIOM = 0
    HYPOTHESIS = 1
    DEFINITION = 2
    ASSUMPTION = 3
    LEMMA = 4
    THEOREM = 5
    COROLLARY = 6
    CONJECTURE = 7
    PLAIN = 8
    FI_DOMAIN = 9
    FI_FUNCTORS = 10
    FI_PREDICATES = 11
    UNKNOWN = 12
    TYPE = 13
    NEGATED_CONJECTURE = 14


class BinaryConnective(Enum):
    CONJUNCTION = 0
    DISJUNCTION = 1
    BIIMPLICATION = 2
    IMPLICATION = 3
    REVERSE_IMPLICATION = 4
    SIMILARITY = 5
    NEGATED_CONJUNCTION = 6
    NEGATED_DISJUNCTION = 7

class DefinedPredicate(Enum):
    DISTINCT = 0
    LESS = 1
    LESS_EQ = 2
    GREATER = 3
    GREATER_EQ = 4
    IS_INT = 5
    IS_RAT = 6
    BOX_P = 7
    BOX_I = 8
    BOX_INT = 9
    BOX = 10
    DIA_P = 11
    DIA_I = 12
    DIA_INT = 13
    DIA = 14

class QuantifiedFormula(TPTPElement):
    def __init__(self, quantifier, variables, formula):
        self.quantifier = quantifier
        self.variables = variables
        self.formula = formula


class AnnotatedFormula(TPTPElement):
    def __init__(self, name, role: FormulaRole, formula):
        self.name = name
        self.role = role
        self.formula = formula


class BinaryFormula(TPTPElement):
    def __init__(self, left, operator, right):
        self.left = left
        self.right = right
        self.operator = operator

class FunctorExpression(TPTPElement):
    def __init__(self, functor, arguments):
        self.functor = functor
        self.arguments = arguments


class PredicateExpression(TPTPElement):
    def __init__(self, predicate, arguments):
        self.predicate = predicate
        self.arguments = arguments
