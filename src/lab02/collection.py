import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *
from src.lab02.validate import *

class StudentGroup:
    name: str
    _items: list[Student]
    
    def __init__(self, name: str):
        collection_validate_init(self, name)
        self.name = name
        self._items = []
    
    def add(self, student: Student):
        collection_validate_add(self._items, student)
        if not isinstance(student, Student):
            raise TypeError("not a student")
        if (student.student_group != self.name):
            raise ValueError("group name mismatch")
        self._items.append(student)

    def remove(self, student): 
        collection_validate_remove(self._items, student)
        self._items.remove(student)
    
    def remove_at(self, index):
        collection_validate_remove_at(self._items, index)
        return self._items.pop(index)
    
    def get_all(self):
        return self._items.copy()
    
    def find_by_name(self, name):
        for student in self._items:
            if student.student_name.lower() == name.lower():
                return student
        return None
    
    def find_by_course(self, course):
        return [s for s in self._items if s.student_course == course]
    
    def find_by_gpa(self, gpa):
        return [s for s in self._items if s.student_gpa == gpa]
    
    def __len__(self): 
        return len(self._items)
    
    def __iter__(self): 
        return iter(self._items)
    
    def __getitem__(self, index): 
        if isinstance(index, slice):
            new_group = StudentGroup(StudentGroup.name)
            for student in self._items[index]:
                new_group.add(student)
            return new_group
        return self._items[index]
    
    def __contains__(self, student):
        return student in self._items
    
    def __str__(self):
        if not self._items:
            return "empty!"
        result = f"{self.name} contains {len(self._items)} students:\n"
        result += "-" * 40 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.student_name} (GPA: {student.student_gpa}, course: {student.course})\n"
        return result
    
    def sort_by_name(self, reverse=False): 
        self._items.sort(key=lambda s: s.student_name, reverse=reverse)
    
    def sort_by_course(self, reverse=False): 
        self._items.sort(key=lambda s: s.student_course, reverse=reverse)
    
    def sort_by_gpa(self, reverse=False): 
        self._items.sort(key=lambda s: s.student_gpa, reverse=reverse)
    
    def sort(self, key, reverse=False):
        self._items.sort(key=key, reverse=reverse)

    def get_active(self):
        new_group = StudentGroup(self.name)
        for student in self._items:
            if student.active:
                new_group.add(student)
        return new_group
    
    def get_top(self):
        new_group = StudentGroup(self.name)
        for student in self._items:
            if student.student_gpa >= 4.5:
                new_group.add(student)
        return new_group
    
    def get_course(self, course):
        new_group = StudentGroup(self.name)
        for student in self._items:
            if student.course == course:
                new_group.add(student)
        return new_group