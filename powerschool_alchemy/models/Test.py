from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base

class Test(Base):
    __tablename__ = 'test'
    
    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    test_scores = relationship('TestScore', back_populates='test')

    def __repr__(self):
        return 'Test: ' + pformat(vars(self))
