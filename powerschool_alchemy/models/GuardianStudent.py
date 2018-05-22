from pprint import pformat
from sqlalchemy import (Column, ForeignKey, Integer, String, ForeignKeyConstraint)
from sqlalchemy.orm import relationship

from .base import Base


class GuardianStudent(Base):
    __tablename__ = 'guardianstudent'

    guardian_student_id = Column('guardianstudentid', Integer, primary_key=True)
    guardian_id = Column('guardianid', Integer, ForeignKey('guardian.guardianid'))
    student_dcid = Column('studentsdcid', Integer, ForeignKey('students.dcid'))
    guardian = relationship('Guardian', back_populates='students')
    student = relationship('Student', back_populates='guardians')

    def __repr__(self):
        return 'GuadianStudent: ' + pformat(vars(self))
