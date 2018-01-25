from pprint import pformat

from sqlalchemy import (Column, Integer, String)

from .base import Base


class AttendanceCode(Base):
    __tablename__ = 'attendance_code'

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    presence_status_code = Column('presence_status_cd', String)
    attendance_code = Column('att_code', String)

    def __repr__(self):
        return 'Attendance Code: ' + pformat(vars(self))
