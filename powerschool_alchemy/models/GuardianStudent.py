from pprint import pformat

from sqlalchemy import (Column, ForeignKey, Integer)
from sqlalchemy.orm import relationship

from .base import Base

class GuardianStudent(Base):
    __tablename__ = 'GuardianStudent'
    
    guardian_student_id = Column('guardianstudentid', Integer, primary_key=True)
    guardian_id = Column('guardianid', Integer, ForeignKey('guardian.accountidentifier'))
    student_dcid = Column('studentsdcid', Integer, ForeignKey('students.dcid'))

    def __repr__(self):
        return 'GuadianStudent: ' + pformat(vars(self))