import sqlalchemy as sqla
from sqlalchemy.orm import relation
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Formula(Base):
    id = sqla.Column(sqla.Integer, primary_key=True)
    string = sqla.Column(sqla.String)


class SolutionItem(Base):
    premise = sqla.Column(sqla.Integer, sqla.ForeignKey(Formula.id))
    used = sqla.Column(sqla.Boolean)


class Solution(Base):
    premises = relation(SolutionItem)


class Problem(Base):
    conjecture = sqla.Column(sqla.Integer, sqla.ForeignKey(Formula.id))
    premises = relation(Formula)
    solutions = relation(Solution)