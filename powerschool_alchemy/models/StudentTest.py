from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .Term import Term
from .Student import Student
from .Test import Test
from .StudentCoreField import StudentCoreField
from .base import Base


class StudentTest(Base):
    __tablename__ = 'studenttest'
    __table_args__ = (
        ForeignKeyConstraint(
            ['termid', 'schoolid'],
            ['terms.id', 'terms.schoolid']
        ),
        ForeignKeyConstraint(
            ['studentid'],
            ['students.id']
        ),
        ForeignKeyConstraint(
            ['testid'],
            ['test.id']
        ),
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
    student_test_scores = relationship(
        'StudentTestScore', back_populates='student_test')

    def __repr__(self):
        return 'StudentTest: ' + pformat(vars(self))
