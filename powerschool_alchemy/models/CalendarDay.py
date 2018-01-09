from pprint import pformat
from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base


class CalendarDay(Base):
    __tablename__ = 'calendar_day'

    id = Column(Integer)
    dcid = Column(Integer, primary_key=True)
    date_value = Column(Date)
    school_id = Column('schoolid', Integer)
    in_session = Column('insession', Boolean)

    def __repr__(self):
            return 'CalendarDay: ' + pformat(vars(self))
