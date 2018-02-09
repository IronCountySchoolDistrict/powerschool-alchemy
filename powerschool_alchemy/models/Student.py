from pprint import pformat

from sqlalchemy import (Column, Date, Float,
                        ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship
from .base import Base


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
        ForeignKeyConstraint(
            ['dcid'],
            ['studentcorefields.studentsdcid']
        )
    )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    lastfirst = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    student_number = Column(Float)
    enroll_status = Column(Integer)
    grade_level = Column(String)
    gender = Column(String)
    state_studentnumber = Column(String(length=32))
    entry_date = Column('entrydate', Date)
    exit_date = Column('exitdate', Date)
    father = Column(String)
    mother = Column(String)
    home_phone = Column(String)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    date_of_birth = Column('dob', Date)
    core_fields = relationship('StudentCoreField', uselist=False)

    @property
    def full_name(self):
        full_name = ''
        full_name += self.first_name
        if self.middle_name:
            full_name += ' ' + self.middle_name
        full_name += ' ' + self.last_name
        return full_name

    def __repr__(self):
        return 'Student: ' + pformat(vars(self))
