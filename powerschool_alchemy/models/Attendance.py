from pprint import pformat

from sqlalchemy import (Column, Date, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Attendance(Base):
    __tablename__ = 'attendance'
    __table_args__ = (
        ForeignKeyConstraint(['ccid'], ['cc.id']),
        ForeignKeyConstraint(['studentid'], ['students.id']),
        ForeignKeyConstraint(['attendance_codeid'], ['attendance_code.id']),
        ForeignKeyConstraint(['periodid'], ['period.id']),
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
