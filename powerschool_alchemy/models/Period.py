from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Period(Base):
    __tablename__ = 'period'
    __table_args__ = (ForeignKeyConstraint(['schoolid'], ['schools.school_number']), )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    year_id = Column('year_id', Integer)
    period_number = Column(Integer)
    name = Column(String)
    abbreviation = Column(String)

    def __repr__(self):
        return 'Period: ' + pformat(vars(self))
