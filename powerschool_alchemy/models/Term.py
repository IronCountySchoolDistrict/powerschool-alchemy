from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship
from .base import Base


class Term(Base):
    __tablename__ = 'terms'
    __table_args__ = (ForeignKeyConstraint(['schoolid'], ['schools.school_number']), )

    id = Column(Integer)
    year_id = Column('yearid', Integer)
    name = Column(String)
    dcid = Column(Integer, primary_key=True)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    first_day = Column('firstday', Date)
    last_day = Column('lastday', Date)
    is_year = Column('isyearrec', Boolean)

    def __repr__(self):
        return 'Term: ' + pformat(vars(self))
