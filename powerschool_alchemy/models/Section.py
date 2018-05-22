from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Section(Base):
    __tablename__ = 'sections'
    __table_args__ = (
        ForeignKeyConstraint(['course_number'], ['courses.course_number']),
        ForeignKeyConstraint(['termid', 'schoolid'], ['terms.id', 'terms.schoolid']),
        ForeignKeyConstraint(['schoolid'], ['schools.school_number']),
    )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    course_number = Column(String)
    course = relationship('Course')
    term_id = Column('termid', Integer)
    term = relationship('Term')
    school_id = Column('schoolid', Integer)
    school = relationship('School', viewonly=True)
    teacher_id = Column('teacher', Integer)
    external_expression = Column(String)
    section_meetings = relationship('SectionMeeting', back_populates='section')

    def __repr__(self):
        return 'Section: ' + pformat(vars(self))
