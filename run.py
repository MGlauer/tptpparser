from data.io.structures import create_tables, drop_tables
from language.tptp.build import load_problems, load_axiomsets


if __name__ == '__main__':
    drop_tables()
    create_tables()
    load_axiomsets()
    load_problems()