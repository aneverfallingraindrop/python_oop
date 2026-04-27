import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from datetime import date 
from src.lab01.validate import *
class Student: 
    course: int
    personal_info: list  # [name: str, age: int, group: str]
    gpa: float
    active: bool
    sick_leave_log: list
    _grades: list
    _scholarship: bool

    def __init__(self, name: str, age: int, group: str, course: int):
        validate_init(name, age, group, course)
        self.personal_info = [name, age, group]
        self.course = course
        self.gpa = 0
        self.active = True
        self.sick_leave_log = []
        self._grades = []
        self._scholarship = False
    
    def grade(self, grade: int) -> None:
        validate_grade(self, grade)
        self._grades.append(grade)
        self.gpa = float(f'{round(sum(self._grades)/len(self._grades), 1):.1f}') # some institutions trunctuate, some round. we round. we spheres in here.
        
    def add_sick_leave(self, start: date, end: date) -> None:
        validate_add_sick_leave(self, start, end)
        self.sick_leave_log.append([start, end])
    
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.personal_info[2] = '' #removing group once inactive
        self.active = False

    def upgrade_course(self) -> None:
        if self.student_course >= 6:
            raise Exception("time 2 graduate")
        self.update_course += 1  
    
    def grant_scholarship(self):
        if not self.active:
            return "Student inactive"
        if self.student_gpa > 4.0: 
            self._scholarship = True
            return("Granted!")
        else: return f"GPA has to be over 4.0 (currently {self.student_gpa})"
    
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
    
    @property
    def student_gpa(self) -> float:
        return self.gpa
    
    @property
    def student_course(self) -> int:
        return self.course

    @student_name.setter
    def update_name(self, new_name: str) -> None:
        validate_name_setter(new_name)
        self.personal_info[0] = new_name
    
    @student_age.setter
    def update_age(self, new_age: int) -> None:
        validate_age_setter(self, new_age)
        self.personal_info[1] = new_age
    
    @student_group.setter
    def update_group(self, new_group: str) -> None:
        validate_group_setter(self, new_group)
        self.personal_info[2] = new_group

    @student_course.setter
    def update_course(self, new_course: int) -> None:
        validate_course_setter(self, new_course)
        self.course = new_course

    def unittest_update_name(self, new_name: str) -> None:
        self.update_name = new_name
    
    def unittest_update_age(self, new_age: int) -> None:
        self.update_age = new_age
    
    def unittest_update_group(self, new_group: str) -> None:
        self.update_group = new_group

    def unittest_update_course(self, new_course: int) -> None:
        self.update_course = new_course

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


