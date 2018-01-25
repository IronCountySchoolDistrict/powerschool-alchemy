from pprint import pformat

from sqlalchemy import (Column, Float, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = (
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
    )

    dcid = Column(Integer, primary_key=True)
    name = Column('course_name', String)
    code = Column(String)
    number = Column('course_number', String)
    credit_hours = Column(Float)
    school_id = Column('schoolid', Integer)
    school = relationship('School')

    def __repr__(self):
        return 'Course: ' + pformat(vars(self))
