from pprint import pformat

from sqlalchemy import (Column, Float, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship
from .base import Base


class StudentTestScore(Base):
    __tablename__ = 'studenttestscore'
    __table_args__ = (
        ForeignKeyConstraint(['studenttestid'], ['studenttest.id']),
        ForeignKeyConstraint(['testscoreid'], ['testscore.id']),
    )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    test_score_id = Column('testscoreid', Integer)
    student_test_id = Column('studenttestid', Integer)
    alpha_score = Column('alphascore', String)
    num_score = Column('numscore', Float)
    percent_score = Column('percentscore', Float)

    student_test = relationship(
        'StudentTest', back_populates='student_test_scores')
    test_score = relationship('TestScore')

    def __repr__(self):
        return 'StudentTestScore: ' + pformat(vars(self))
