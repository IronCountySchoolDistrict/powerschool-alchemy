from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base

class School(Base):
    __tablename__ = 'schools'

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    name = Column(String)
    school_number = Column(String, unique=True)
    
    def __repr__(self):
        return 'School: ' + pformat(vars(self))
