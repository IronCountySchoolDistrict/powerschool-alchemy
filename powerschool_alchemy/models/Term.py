from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .School import School
from .base import Base

class Term(Base):
    __tablename__ = 'terms'
    __table_args__ = (
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
    )

    id = Column(Integer)
    year_id = Column('yearid', Integer)
    name = Column(String)
    dcid = Column(Integer, primary_key=True)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    first_day = Column('firstday', Date)
    last_day = Column('lastday', Date)
    is_year = Column('isyearrec', Boolean)
    year_id = Column('yearid', Integer)

    def __repr__(self):
        return 'Term: ' + pformat(vars(self))
    