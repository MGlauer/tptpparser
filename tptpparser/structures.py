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