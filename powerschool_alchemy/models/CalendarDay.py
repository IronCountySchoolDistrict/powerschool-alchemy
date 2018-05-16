from pprint import pformat
from sqlalchemy import (Boolean, ForeignKeyConstraint, Column, Date, Integer)
from sqlalchemy.orm import relationship

from .base import Base


class CalendarDay(Base):
    __tablename__ = 'calendar_day'
    __table_args__ = (
        ForeignKeyConstraint(['schoolid'], ['schools.school_number']),
        ForeignKeyConstraint(['cycle_day_id'], ['cycle_day.id'],
        ),
    )

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    date_value = Column(Date)
    school_id = Column('schoolid', Integer)
    in_session = Column('insession', Boolean)
    cycle_day_id = Column(Integer)
    cycle_day = relationship('CycleDay', viewonly=True)

    school = relationship('School')

    def __repr__(self):
        return 'CalendarDay: ' + pformat(vars(self))
