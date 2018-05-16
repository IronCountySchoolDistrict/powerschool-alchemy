from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer)
from sqlalchemy.orm import relationship

from .base import Base


class SchoolCourse(Base):
    __tablename__ = 'school_course'
    __table_args__ = (
        ForeignKeyConstraint(['schoolid'], ['schools.school_number']),
        ForeignKeyConstraint(['courseid'], ['courses.id']),
        ForeignKeyConstraint(
            ['schoolid', 'yearid'], 
            ['terms.schoolid', 'terms.yearid']),
    )

    # id = Column(Integer, unique=True)
    dcid = Column(Integer, primary_key=True)
    school_id = Column('schoolid', Integer)
    course_id = Column('courseid', Integer)
    year_id = Column('yearid', Integer)
    status = Column('status', Integer)

    term = relationship(
        'Term',
        primaryjoin=
        "and_(SchoolCourse.year_id==Term.year_id, SchoolCourse.school_id==Term.school_id, Term.is_year==True)",
        viewonly=True
    )
    school = relationship('School', viewonly=True)
    course = relationship('Course', back_populates='school_courses')

    def __repr__(self):
        return 'SchoolCourse: ' + pformat(vars(self))
