from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class TestScore(Base):
    __tablename__ = 'testscore'
    __table_args__ = (ForeignKeyConstraint(['testid'], ['test.id']), )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    test_id = Column('testid', Integer)
    name = Column(String)
    description = Column(String)
    sort_order = Column('sortorder', Integer)

    test = relationship('Test', back_populates='test_scores')

    def __repr__(self):
        return 'TestScore: ' + pformat(vars(self))
