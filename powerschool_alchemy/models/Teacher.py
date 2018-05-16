from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    __table_args__ = (ForeignKeyConstraint(['schoolid'], ['schools.school_number']), )

    dcid = Column(Integer, primary_key=True)
    id = Column(Integer)
    last_first = Column('lastfirst', String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    school_id = Column('schoolid', Integer)
    school = relationship('School')
    status = Column(Integer)
    email_address = Column('email_addr', String)

    def __repr__(self):
        return 'Teacher: ' + pformat(vars(self))
