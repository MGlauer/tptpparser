import os
from antlr4 import *
from language.tptp.parser.tptp_v7_0_0_0Lexer import tptp_v7_0_0_0Lexer
from language.tptp.parser.tptp_v7_0_0_0Parser import tptp_v7_0_0_0Parser
from language.tptp.flattening import FOFFlatteningVisitor
import data.io.structures as db
from data.io.connection import get_engine
from logic import fol
import pickle as pkl
import sys
sys.setrecursionlimit(10000)
import sqlalchemy as sqla
from sqlalchemy.orm.session import sessionmaker

def load_folder(path, processor):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if not file =='README':
                    f = os.path.join(root,file)
                    processor(session, f)
                session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def load_problems():
    return load_folder('data/TPTP/Problems', load_problem)


def load_problem(session, path):
    problem = db.Problem()
    for line in load_file(path):
        if isinstance(line, fol.Import):
            import_path = None
            for imported_line in load_file(import_path):
                l = store_formula(session, imported_line)
                problem.premises.append(l.id)
        else:
            conjecture = store_formula(session, line)
            problem.conjecture = conjecture.id
    session.add(problem)


def store_formula(session, formula, source=None):
    result = db.Formula(blob=pkl.dumps(formula), source=source.id)
    session.add(result)
    return result


def load_axiomsets():
    load_folder('data/TPTP/Axioms', load_axiomset)


def load_axiomset(session, path):
    source = db.Source(path=path)
    session.add(source)
    for item in load_file(path):
        axiom = store_formula(session, item, source=source)
        session.add(axiom)
        session.commit()


def load_file(path):
    print(path)
    input = FileStream(path)
    lexer = tptp_v7_0_0_0Lexer(input)
    stream = CommonTokenStream(lexer)
    print('initialise parser...')
    parser = tptp_v7_0_0_0Parser(stream)
    print('done')
    print('build parse tree...')
    visitor = FOFFlatteningVisitor()
    # result = visitor.visit(parser.tptp_file())
    tree = parser.tptp_input()
    done = False
    i=0
    while tree and not done:
        i += 1
        if i%10000==0:
            print(i, tree.getText())
        try:
            yield visitor.visit(tree)
        except fol.EOFException:
            done = True
        else:
            tree = parser.tptp_input()