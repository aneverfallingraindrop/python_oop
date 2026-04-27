import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *
from src.lab04.interfaces import *

class BachelorStudent(Student, Comparable, Printable):
    
    def __init__(self, name, age, group, course, specialty, has_practice=False):
        super().__init__(name, age, group, course)
        self._specialty = specialty
        self._has_practice = has_practice
    
    @property
    def specialization(self):
        return self._specialty
    
    @property
    def has_practice(self):
        return self._has_practice
    
    def complete_practice(self):
        if not self.active:
            raise Exception("inactive student cannot finish practice")
        if self._has_practice:
            return "practice already finished"
        self._has_practice = True
        return f"{self.student_name} has successfully finished the practice"
    
    def upgrade_course(self):
        if self.student_course >= 4:
            raise Exception("time 2 graduate")
        super().update_course += 1  # base class method 
    
    def __str__(self):
        parent_str = super().__str__()
        practice_status = "Yes" if self._has_practice else "No"
        return (f"{parent_str}\n"
                f"  Specialty: {self._specialty}\n"
                f"  Practice: {practice_status}\n"
                f"  Scholarship: {self._scholarship}")

    def compare_to(self, other):
        if not isinstance(other, BachelorStudent):
            return -1
        if self.student_gpa < other.student_gpa:
            return -1
        elif self.student_gpa > other.student_gpa:
            return 1
        return 0

    def to_string(self):
        return(f"Name: {self.student_name}, Age: {self.student_age}, Group: {self.student_group}, Course: {self.student_course}")


class MasterStudent(Student, Comparable, Printable):
    
    def __init__(self, name, age, group, course, research, thesis=False, scholarship = False):
        super().__init__(name, age, group, course)
        self._research_topic = research
        self._thesis = thesis
        self._scholarship = scholarship
    
    @property
    def research_topic(self):
        return self._research_topic
    
    @property
    def has_thesis(self):
        return self._thesis
    
    def defend_thesis(self):
        if not self.active:
            raise Exception("inactive student cannot defend thesis")
        if self._thesis:
            return "thesis already defended"
        self._thesis = True
        return f"{self.student_name} has successfully finished their thesis on the topic: '{self._research_topic}'."
    
    def grant_scholarship(self):
        if not self.active:
            raise ValueError("Inactive student")
        if self.student_gpa > 4.2: 
            self._scholarship = True
            return("Granted!")
        else: return f"GPA has to be over 4.2 (currently {self.student_gpa})"
    
    def __str__(self):
        parent_str = super().__str__()
        thesis_status = "Yes" if self._thesis else "No"
        return (f"{parent_str}\n"
                f"  Research topic:: {self._research_topic}\n"
                f"  Thesis: {thesis_status}\n"
                f"  Scholarship: {thesis_status}")
    
    def compare_to(self, other):
        if not isinstance(other, MasterStudent):
            return -1
        if self._scholarship < other._scholarship:
            return -1
        elif self._scholarship > other._scholarship:
            return 1
        return 0

    def to_string(self):
        return(f"Name: {self.student_name}, Research: {self.research_topic}, Thesis: {self.has_thesis}, Scholarship: {self._scholarship}")


class PhDStudent(Student, Comparable, Printable):
    def __init__(self, name, age, group, course, research, publications=0, scholarship = False):
        super().__init__(name, age, group, course)
        self._research = research
        self._publications = publications
        self._scholarship = scholarship
    
    @property
    def research_area(self):
        return self._research
    
    @property
    def publications(self):
        return self._publications
    
    def publish_article(self):
        if not self.active:
            raise Exception("inactive student cannot publish")
        self._publications += 1
        return f"{self.student_name} has successfully published article number {self.publications} regarding '{self._research}'."
    
    def grant_scholarship(self):
        if not self.active:
            return "Student inactive"
        self._scholarship = True
        return "Granted!" 
    
    def __str__(self):
        parent_str = super().__str__()
        return (f"{parent_str}\n"
                f"  Research area: {self._research}\n"
                f"  Times published: {self._publications}\n"
                f"  Scholarship: {self._scholarship}")
    
    def compare_to(self, other):
        if not isinstance(other, PhDStudent):
            return -1
        if self.publications < other.publications:
            return -1
        elif self.publications > other.publications:
            return 1
        return 0

    def to_string(self):
        return(f"Name: {self.student_name}, Research: {self.research_area}, Publications: {self.publications}, Scholarship: {self._scholarship}")