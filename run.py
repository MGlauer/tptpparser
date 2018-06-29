import sys, os
from antlr4 import *
from parser.tptp_v7_0_0_0Lexer import tptp_v7_0_0_0Lexer
from parser.tptp_v7_0_0_0Parser import tptp_v7_0_0_0Parser
from tptpparser.flattening import FOFFlatteningVisitor

def main(path):
    input = FileStream(path)
    lexer = tptp_v7_0_0_0Lexer(input)
    stream = CommonTokenStream(lexer)
    print('initialise parser...')
    parser = tptp_v7_0_0_0Parser(stream)
    print('done')
    print('build parse tree...')
    tree = parser.tptp_file()
    print('done')
    visitor = FOFFlatteningVisitor()
    result = visitor.visit(tree)
    for line in result:
        print(line)


if __name__ == '__main__':
    for root, dirs, files in os.walk('data/TPTP-v7.1.0/Axioms'):
        for file in files:
            if not file =='README':
                f = os.path.join(root,file)
                print(f)
                main(f)