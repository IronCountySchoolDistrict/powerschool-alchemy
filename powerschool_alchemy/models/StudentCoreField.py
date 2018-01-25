from pprint import pformat

from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship
from .base import Base


class StudentCoreField(Base):
    __tablename__ = 'studentcorefields'

    student_dcid = Column('studentsdcid', Integer, primary_key=True)
    student = relationship('Student', back_populates='core_fields')
    father_home_phone = Column(String(length=4000))
    father_day_phone = Column('fatherdayphone', String(length=4000))
    mother_home_phone = Column(String(length=4000))
    mother_day_phone = Column('motherdayphone', String(length=4000))

    def __repr__(self):
            return 'StudentCoreField: ' + pformat(vars(self))
