from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .CC import CC
from .Student import Student
from .AttendanceCode import AttendanceCode
from .Period import Period
from .base import Base

class Attendance(Base):
    __tablename__ = 'attendance'
    __table_args__ = (
        ForeignKeyConstraint(
            ['ccid'],
            ['cc.id']
        ),
        ForeignKeyConstraint(
            ['studentid'],
            ['students.id']
        ),
        ForeignKeyConstraint(
            ['attendance_codeid'],
            ['attendance_code.id']
        ),
        ForeignKeyConstraint(
            ['periodid'],
            ['period.id']
        ),
    )

    dcid = Column(Integer, primary_key=True)
    cc_id = Column('ccid', Integer)
    cc = relationship('CC')
    student_id = Column('studentid', String)
    student = relationship('Student')
    attendance_code_id = Column('attendance_codeid', Integer)
    code = relationship('AttendanceCode')
    period_id = Column('periodid')
    period = relationship('Period')
    date = Column('att_date', Date)

    def __repr__(self):
        return 'Attendance: ' + pformat(vars(self))
