from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base
from .Test import Test

class TestScore(Base):
    __tablename__ = 'testscore'
    __table_args__ = (
        ForeignKeyConstraint(
            ['testid'],
            ['test.id']
        ),
    )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    test_id = Column('testid', Integer)
    name = Column(String)
    description = Column(String)
    sort_order = Column('sortorder', Integer)

    test = relationship('Test', back_populates='test_scores')

    def __repr__(self):
        return 'TestScore: ' + pformat(vars(self))
