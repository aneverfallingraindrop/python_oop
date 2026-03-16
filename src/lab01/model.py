from datetime import date 

class Student: 
    course: int
    personal_info: list  # [name: str, age: int, group: str]
    gpa: float
    active: bool
    sick_leave_log: list
    _grades: list
  
    
    def __init__(self, name: str, age: int, group: str, course: int):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 6 or age > 100: # a six year-old has somehow started college in South Alabama, graduating at ten. what a world
            raise ValueError("Age must be an integer between 6 and 100.")
        if not isinstance(group, str) or len(group.strip()) == 0:
            raise ValueError("Group must be a non-empty string.") # can only be empty if the student is on academic leave aka inactive
        if not isinstance(course, int) or course < 1 or course > 6:
            raise ValueError("Course must be an integer between 1 and 6.") 

        self.personal_info = [name, age, group]
        self.course = course
        self.gpa = 0
        self.active = True
        self.sick_leave_log = []
        self._grades = []
    
    def grade(self, grade: int) -> None:
        if not isinstance(grade, int) or grade > 5 or grade < 2:
            raise ValueError('Invalid grade! Must be an integer between 2 and 5.') # on technicality, a 0 is also possible as per just not submitting a task. but we dont care do we
        if self.active == False:
            raise AttributeError('Student must be active in order to grade...') # what kinda task can you grade when theyre on academic leave
        self._grades.append(grade)
        self.gpa = float(f'{round(sum(self._grades)/len(self._grades), 1):.1f}') # some institutions trunctuate, some round. we round. we spheres in here.
        
    @property
    def student_gpa(self) -> float:
        return self.gpa

    def add_sick_leave(self, start: date, end: date) -> None:
        if not isinstance(start, date):
            raise ValueError('Invalid leave start.') 
        if not isinstance(end, date):
            raise ValueError('Invalid leave end.')
        if end < start:
            raise ValueError('Invalid leave dates!')
        if self.active == False:
            raise AttributeError('Student inactive, sick leaves during this period dont matter.')
        self.sick_leave_log.append([start, end])
    
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.personal_info[2] = '' #removing group once inactive
        self.active = False
    
    def update_name(self, new_name: str) -> None:
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.personal_info[0] = new_name
    
    def update_age(self, new_age: int) -> None:
        if not isinstance(new_age, int) or new_age < 6 or new_age > 100: 
            raise ValueError("Age must be an integer between 6 and 100.")
        if new_age < self.personal_info[1]:
            raise ValueError("Age cannot decrease.")
        self.personal_info[1] = new_age
    
    def update_group(self, new_group: str) -> None:
        if not isinstance(new_group, str) or len(new_group.strip()) == 0:
            raise ValueError("Group must be a non-empty string.")
        if self.active == False:
            raise AttributeError('Student must be active in order to update group.')
        self.personal_info[2] = new_group

    def update_course(self, new_course: int) -> None:
        if not isinstance(new_course, int) or new_course < 1 or new_course > 6:
            raise ValueError("Course must be an integer between 1 and 6.")
        if new_course < self.course:
            raise ValueError('Course cannot decrease.')
        self.course = new_course

    @property    
    def student_name(self) -> str:
        return self.personal_info[0]
    
    @property
    def student_age(self) -> int:
        return self.personal_info[1]
    
    @property
    def student_group(self) -> str:
        return self.personal_info[2]
    
    @property
    def student_sick_leave_log(self) -> list:
        return self.sick_leave_log

    def __repr__(self):
        return (f"Student(name='{self.personal_info[0]}', age={self.personal_info[1]}, "
                f"group='{self.personal_info[2]}', course='{self.course}', "
                f"gpa={self.gpa:.1f}, active={self.active}, "
                f"sick_leave_log={self.sick_leave_log})")
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.personal_info[0] == other.personal_info[0] and 
                self.personal_info[1] == other.personal_info[1] and
                self.course == other.course) # we can add a group check, but it'd be redundant. same name, DOB and course tell us enough.

    def __str__(self):
        return f"Person: {self.personal_info[0]}, Age: {self.personal_info[1]}, Group: {self.personal_info[2]},\nCourse: {self.course}, GPA: {self.gpa}."
    