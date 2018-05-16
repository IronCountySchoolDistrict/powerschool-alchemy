from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class SectionMeeting(Base):
    __tablename__ = 'section_meeting'
    __table_args__ = (
        ForeignKeyConstraint(['schoolid'], ['schools.school_number']),
        ForeignKeyConstraint(['sectionid'], ['sections.id']),
        ForeignKeyConstraint(
            ['schoolid', 'cycle_day_letter', 'year_id'],
            ['cycle_day.schoolid', 'cycle_day.letter', 'cycle_day.year_id']
        )
    )

    dcid = Column(Integer, primary_key=True)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    year_id = Column(Integer)
    section_id = Column('sectionid', Integer)
    period_number = Column(Integer)
    cycle_day_letter = Column(String)
    section = relationship(
        'Section', back_populates='section_meetings')
    cycle_day = relationship('CycleDay', viewonly=True)

    def __repr__(self):
        return 'SectionMeeting: ' + pformat(vars(self))
