from pprint import pformat

from sqlalchemy import (Column, ForeignKeyConstraint, Integer, String)
from sqlalchemy.orm import relationship

from .base import Base


class Guardian(Base):
    __tablename__ = 'guardian'

    guardian_id = Column('guardianid', Integer, primary_key=True)
    first_name = Column('firstname', String)
    middle_name = Column('middlename', String)
    last_name = Column('lastname', String)
    students = relationship('GuardianStudent', back_populates='guardian')

    @property
    def full_name(self):
        if self.middle_name:
            fullname = '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)
        else:
            fullname = '{} {}'.format(self.first_name, self.last_name)
        return fullname

    def __repr__(self):
        return 'Guadian: ' + pformat(vars(self))
