from pprint import pformat
from sqlalchemy import (Boolean, ForeignKeyConstraint, Column, Date, Integer)
from sqlalchemy.orm import relationship

from .base import Base


class CalendarDay(Base):
    __tablename__ = 'calendar_day'
    __table_args__ = (
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
    )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    date_value = Column(Date)
    school_id = Column('schoolid', Integer)
    in_session = Column('insession', Boolean)

    school = relationship('School')

    def __repr__(self):
            return 'CalendarDay: ' + pformat(vars(self))
