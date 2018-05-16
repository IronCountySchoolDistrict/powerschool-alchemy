from pprint import pformat

from sqlalchemy import (Column, Date, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class CC(Base):
    __tablename__ = 'cc'
    __table_args__ = (
        ForeignKeyConstraint(['studentid'], ['students.id']),
        ForeignKeyConstraint(['schoolid'], ['schools.school_number']),
        ForeignKeyConstraint(
            ['termid', 'schoolid'], 
            ['terms.id', 'terms.schoolid']),
    )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    student_id = Column('studentid', Integer)
    student = relationship('Student')
    section_id = Column('sectionid', Integer)
    # The CC.section_id value is negated when a student drops the course
    # primaryjoin here checks for sectionids that were negated
    section = relationship(
        'Section',
        viewonly=True,
        primaryjoin="and_("
        "or_(Section.id==CC.section_id, Section.id==-CC.section_id), "
        "Term.school_id==CC.school_id)"
    )
    course_number = Column(String)
    date_enrolled = Column('dateenrolled', Date)
    date_left = Column('dateleft', Date)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    term_id = Column('termid', Integer)
    # The CC.term_id value is negated when a student drops the course
    # primaryjoin here checks for termids that were negated
    term = relationship(
        'Term',
        viewonly=True,
        primaryjoin="and_("
        "or_(Term.id==CC.term_id, Term.id==-CC.term_id), "
        "Term.school_id==CC.school_id)"
    )
    current_absences = Column('currentabsences', Integer)
    current_tardies = Column('currenttardies', Integer)
    teacher_id = Column('teacherid', Integer)
    expression = Column(String)

    def __repr__(self):
        return 'CC: ' + pformat(vars(self))