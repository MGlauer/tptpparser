from sqlalchemy import create_engine
from settings import DB_CONNECTION

__ENGINE = None

def get_engine():
    global __ENGINE
    if __ENGINE is None:
        if 'password' in DB_CONNECTION:
            cred = '{user}:{password}'.format(**DB_CONNECTION)
        else:
            cred = '{user}'.format(**DB_CONNECTION)
        __ENGINE = create_engine('postgresql://{cred}@{host}:{port}/{database}'.format(
            cred=cred,
            **DB_CONNECTION
        ))
    return __ENGINE
