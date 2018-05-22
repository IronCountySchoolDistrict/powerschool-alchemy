from pprint import pformat
from sqlalchemy import (Boolean, ForeignKeyConstraint, Column, String, Date, Integer)
from sqlalchemy.orm import relationship

from .base import Base


class CycleDay(Base):
    __tablename__ = 'cycle_day'
    __table_args__ = (ForeignKeyConstraint(['schoolid'], ['schools.school_number']), )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    school_id = Column('schoolid', Integer)
    year_id = Column(Integer)
    letter = Column(String)
    day_number = Column(Integer)
    abbreviation = Column(String)
    day_name = Column(String)
    sort_order = Column('sortorder', Integer)

    def __repr__(self):
        return 'CycleDay: ' + pformat(vars(self))