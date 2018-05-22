import os
from pprint import pprint

from dotenv import find_dotenv, load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker

load_dotenv(find_dotenv(usecwd=True))

def create_session() -> Session:
    connect_str = URL(**{
        'drivername': 'oracle',
        "username": os.environ.get('POWERSCHOOL_USER'),
        "password": os.environ.get('POWERSCHOOL_PASSWORD'),
        "host": os.environ.get('POWERSCHOOL_HOST'),
        "port": os.environ.get('POWERSCHOOL_PORT', '1521'),
        "database": os.environ.get('POWERSCHOOL_DATABASE')
    })
    engine = create_engine(connect_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
