from pprint import pformat

from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey,
                        ForeignKeyConstraint, Integer, MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .Term import Term
from .base import Base

class Course(Base):
    __tablename__ = 'courses'
    dcid = Column(Integer, primary_key=True)
    name = Column('course_name', String)
    code = Column(String)
    number = Column('course_number', String)

    def __repr__(self):
        return 'Course: ' + pformat(vars(self))
