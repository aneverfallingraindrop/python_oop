from datetime import date

def validate_init(name: str, age: int, group: str, course: int):
    if not isinstance(name, str) or len(name.strip()) == 0:
        raise ValueError("Name must be a non-empty string.")
    if not isinstance(age, int) or age < 6 or age > 100: # a six year-old has somehow started college in South Alabama, graduating at ten. what a world
        raise ValueError("Age must be an integer between 6 and 100.")
    if not isinstance(group, str) or len(group.strip()) == 0:
        raise ValueError("Group must be a non-empty string.") # can only be empty if the student is on academic leave aka inactive
    if not isinstance(course, int) or course < 1 or course > 6:
        raise ValueError("Course must be an integer between 1 and 6.") 
    
def validate_grade(self, grade: int):
    if not isinstance(grade, int) or grade > 5 or grade < 2:
        raise ValueError('Invalid grade! Must be an integer between 2 and 5.') # on technicality, a 0 is also possible as per just not submitting a task. but we dont care do we
    if self.active == False:
        raise AttributeError('Student must be active in order to grade...') # what kinda task can you grade when theyre on academic leave
    
def validate_add_sick_leave(self, start: date, end: date):
    if not isinstance(start, date):
        raise ValueError('Invalid leave start.') 
    if not isinstance(end, date):
        raise ValueError('Invalid leave end.')
    if end < start:
        raise ValueError('Invalid leave dates!')
    if self.active == False:
        raise AttributeError('Student inactive, sick leaves during this period dont matter.')

def validate_name_setter(new_name: str):
    if not isinstance(new_name, str) or len(new_name.strip()) == 0:
        raise ValueError("Name must be a non-empty string.")

def validate_age_setter(self, new_age: int):
    if not isinstance(new_age, int) or new_age < 6 or new_age > 100: 
        raise ValueError("Age must be an integer between 6 and 100.")
    if new_age < self.personal_info[1]:
        raise ValueError("Age cannot decrease.")

def validate_group_setter(self, new_group: str):
    if not isinstance(new_group, str) or len(new_group.strip()) == 0:
        raise ValueError("Group must be a non-empty string.")
    if self.active == False:
        raise AttributeError('Student must be active in order to update group.')
    
def validate_course_setter(self, new_course: int):
    if not isinstance(new_course, int) or new_course < 1 or new_course > 6:
        raise ValueError("Course must be an integer between 1 and 6.")
    if new_course < self.course:
        raise ValueError('Course cannot decrease.')