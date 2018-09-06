import os
from antlr4 import *
from parser.tptp_v7_0_0_0Lexer import tptp_v7_0_0_0Lexer
from parser.tptp_v7_0_0_0Parser import tptp_v7_0_0_0Parser
from tptpparser.flattening import FOFFlatteningVisitor
from data.io.structures import create_structures

def main(path):
    input = FileStream(path)
    lexer = tptp_v7_0_0_0Lexer(input)
    stream = CommonTokenStream(lexer)
    print('initialise parser...')
    parser = tptp_v7_0_0_0Parser(stream)
    print('done')
    print('build parse tree...')
    visitor = FOFFlatteningVisitor()
    #result = visitor.visit(parser.tptp_file())
    tree = parser.tptp_input()
    while tree:
        yield visitor.visit(tree)
        tree = parser.tptp_input()

def traverse_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file =='README':
                f = os.path.join(root,file)
                print(f)
                for input in main(f):
                    print(input)

if __name__ == '__main__':
    create_structures()
    # traverse_folder('data/TPTP/Axioms')
    #for item in main('data/TPTP/Axioms/CSR002+5.ax'):
    #    print(item)