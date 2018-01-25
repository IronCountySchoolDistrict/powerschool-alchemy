from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class SectionMeeting(Base):
    __tablename__ = 'section_meeting'
    __table_args__ = (
        ForeignKeyConstraint(
            ['schoolid'],
            ['schools.school_number']
        ),
    )

    dcid = Column(Integer, primary_key=True)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    year_id = Column('yearid', Integer)
    section_id = Column('sectionid', Integer)
    period_number = Column(Integer)
    cycle_day_letter = Column(String)

    def __repr__(self):
        return 'SectionMeeting: ' + pformat(vars(self))
