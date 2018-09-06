import enum
import sqlalchemy as sqla
from sqlalchemy.orm import relation
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base
from .connection import get_engine


class Languages(enum.Enum):
    TPTP = 1

Base = declarative_base()


class Formula(Base):
    __tablename__= 'formula'
    id = sqla.Column(sqla.Integer, primary_key=True)
    language = sqla.Column(Enum(Languages))
    string = sqla.Column(sqla.String)


class SolutionItem(Base):
    id = sqla.Column(sqla.Integer, primary_key=True)
    __tablename__ = 'solution_item'
    premise = sqla.Column(sqla.Integer, sqla.ForeignKey(Formula.id))
    used = sqla.Column(sqla.Boolean)


class Solution(Base):
    __tablename__ = 'solution'
    id = sqla.Column(sqla.Integer, primary_key=True)
    premises = relation(SolutionItem)


class Problem(Base):
    __tablename__ = 'problem'
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String, nullable=False, default='')
    conjecture = sqla.Column(sqla.Integer, sqla.ForeignKey(Formula.id))
    premises = relation(Formula)
    solutions = relation(Solution)


def create_structures():
    metadata = Base.metadata
    metadata.bind = get_engine()
    metadata.create_all()


