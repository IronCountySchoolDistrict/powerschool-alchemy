from pprint import pformat

from sqlalchemy import (Column, Integer, String)
from .base import Base


class School(Base):
    __tablename__ = 'schools'

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    name = Column(String)
    school_number = Column(String, unique=True)
    abbreviation = Column(String)
    
    def __repr__(self):
        return 'School: ' + pformat(vars(self))
