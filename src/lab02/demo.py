import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *
from collection import StudentGroup

def main():
    group = StudentGroup('BIVT-25-8')
    
    s1 = Student("student one", 18, "BIVT-25-8", 1)
    s2 = Student("student two", 28, "BIVT-25-8", 2)
    s3 = Student("student three", 38, "BIVT-25-8", 3)
    s4 = Student("student four", 48, "BIVT-25-8", 4)
    s1.grade(2)
    s2.grade(3)
    s3.grade(4)
    s4.grade(5)
    
    group.add(s1)
    group.add(s2)
    group.add(s3)
    group.add(s4)
    
    print("1 — create collection:")
    print(group)
    print("______")

    print("2 — duplicate protection:")
    try:
        s5 = Student("student one", 18, "BIVT-25-8", 1)
        group.add(s5)
    except ValueError as e:
        print(f"error: {e}")
    print("______")
    
    found = group.find_by_name("student one")
    print(f"searching by name 'student one': {found}")
    
    course_students = group.find_by_course(2)
    print(f"getting 2nd course students: {[s.student_name for s in course_students]}")
    print("______")

    print("4 — magic:")
    print(f"amount of students: {len(group)}")
    
    print("iteration through for")
    for student in group:
        print(f"  - {student.student_name} (курс {student.course})")
    
    print(f"first student: {group[0]}")
    print("______")

    print("5 — sorting:")
    group.sort_by_name()
    print("by name:")
    for s in group:
        print(f"  - {s.student_name}")
    
    group.sort_by_gpa(reverse=True)
    print("\nSort by GPA (decreasing):")
    for s in group:
        print(f"  - {s.student_name}: {s.student_gpa}")
    print("______")

    print("6 — filtering:")
    active_group = group.get_active()
    print(f"active: {len(active_group)}")
    
    best = group.get_top()
    print(f"top performance: {[s.student_name for s in best]}")
    print("______")

    print("7 — deleting students:")
    group.remove(s3)
    print(f"after deleting student three: {len(group)}")
    
    removed = group.remove_at(0)
    print(f"deleting index 0: {removed.student_name}")
    print(f"remaining: {len(group)}")
    print("______")

    print("8 — errors:")
    try:
        group.add("not a student") #type: ignore
    except TypeError as e:
        print(f"error: {e}")
    
    try:
        group.remove(s3)
    except ValueError as e:
        print(f"error: {e}")
    
    try:
        group.remove_at(100)
    except IndexError as e:
        print(f"error: {e}")
    print()

    print("9 — collection after everything:")
    print(group)

if __name__ == "__main__":
    main()