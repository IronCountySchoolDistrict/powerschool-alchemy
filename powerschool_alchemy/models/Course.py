from pprint import pformat

from sqlalchemy import (Column, Float, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = (ForeignKeyConstraint(['schoolid'], ['schools.school_number']), )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    name = Column('course_name', String)
    code = Column(String)
    number = Column('course_number', String)
    credit_hours = Column(Float)
    school_id = Column('schoolid', Integer)

    school = relationship('School')
    school_courses = relationship('SchoolCourse')

    @classmethod
    def get_alt_course_number(cls, course_id, session) -> str:
        alt_course_number = session.execute("""SELECT ps_customfields.getcoursescf(id, 'alt_course_number') 
                                            FROM courses 
                                            WHERE courses.id = :course_id""",
                                        {'course_id': course_id}) \
                                .fetchall()
        alt_course_number_result = list(alt_course_number)
        # first [0] refers to the first row. We only expect one row in the result
        # second [0] refers to the alt_course_number field. If that field is blank,
        # it will be set to None by sqlalchemy.
        if alt_course_number_result[0][0]:
            return alt_course_number_result[0][0]
        else:
            return ''

    def __repr__(self):
        return 'Course: ' + pformat(vars(self))
