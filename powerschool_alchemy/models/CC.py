from pprint import pformat

from sqlalchemy import (Column, Date, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class CC(Base):
    __tablename__ = 'cc'
    __table_args__ = (
        ForeignKeyConstraint(
            ['studentid'],
            ['students.id']
        ),
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
        ForeignKeyConstraint(
            ['termid', 'schoolid'],
            ['terms.id', 'terms.schoolid']
        ),
    )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    student_id = Column('studentid', Integer)
    student = relationship('Student')
    section_id = Column('sectionid', Integer)
    course_number = Column(String)
    date_enrolled = Column('dateenrolled', Date)
    date_left = Column('dateleft', Date)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    term_id = Column('termid', Integer)
    term = relationship('Term', viewonly=True)
    current_absences = Column('currentabsences', Integer)
    current_tardies = Column('currenttardies', Integer)
    teacher_id = Column('teacherid', Integer)
    expression = Column(String)

    def __repr__(self):
        return 'CC: ' + pformat(vars(self))
