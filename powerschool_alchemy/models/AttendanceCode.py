from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base

class AttendanceCode(Base):
    __tablename__ = 'attendance_code'

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    presence_status_code = Column('presence_status_cd', String)
    attendance_code = Column('att_code', String)

    def __repr__(self):
        return 'Attendance Code: ' + pformat(vars(self))
