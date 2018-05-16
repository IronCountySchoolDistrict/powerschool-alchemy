from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer)
from sqlalchemy.orm import relationship

from .base import Base


class StudentTest(Base):
    __tablename__ = 'studenttest'
    __table_args__ = (
        ForeignKeyConstraint(
            ['termid', 'schoolid'], 
            ['terms.id', 'terms.schoolid']
        ),
        ForeignKeyConstraint(['studentid'], ['students.id']),
        ForeignKeyConstraint(['testid'], ['test.id']),
    )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    term_id = Column('termid', Integer)
    test_id = Column('testid', Integer)
    school_id = Column('schoolid', Integer)
    student_id = Column('studentid', Integer)

    term = relationship('Term')
    student = relationship('Student')
    test = relationship('Test')
    student_test_scores = relationship('StudentTestScore', back_populates='student_test')

    def __repr__(self):
        return 'StudentTest: ' + pformat(vars(self))
