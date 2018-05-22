powerschool_alchemy
########################################

This library allows you to interact with a PowerSchool Database with SQLALchemy, a Python ORM.


# Usage

.. code:: python

  from powerschool_alchemy.db import create_session 
  from powerschool_alchemy.models import Student, Section, CalendarDay, CC, CycleDay 
  sess = create_session() 
  sess.query(Student).filter(Student.last_name == 'Doe').filter(Student.first_name == 'Jane').first().guardians[0].guardian 
  my_section = sess.query(Section).filter(Section.id==149618).first() 

  section_cal_days = sess \ 
              .query(CalendarDay, CycleDay.letter) \ 
              .join(CycleDay) \ 
              .filter( 
                  CalendarDay.school_id==my_section.school_id,  
                  CalendarDay.date_value >= my_section.term.first_day,  
                  CalendarDay.date_value < my_section.term.last_day, 
                  CycleDay.letter.in_( 
                      list(map(lambda x: x.cycle_day_letter, my_section.section_meetings)))) \ 
              .all() 

  section_cal_days = list(map(lambda x: x[0], section_cal_days)) 
  print(type(section_cal_days))