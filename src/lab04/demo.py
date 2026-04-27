import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *
from src.lab02.collection import *
from models import *

def print_all_printable(items):
    for item in items:
        if isinstance(item, Printable):
            print(item.to_string())
        else:
            print(f"{item} does not use Printable")


def print_separator(title: str = ""):
    print(f"\n{'=' * 60}")
    if title:
        print(f" {title} ".center(60, '='))
    print(f"{'=' * 60}")

def scenario_1():
    print_separator("1: interface call")

    students = [
        BachelorStudent("bayle bachelor", 19, 'hopital', 1, "Programming"),
        MasterStudent("michael masters", 23, 'hopital', 2, "AI"),
        PhDStudent("Gregory House, M.D.", 45, 'hopital', 3, "Medicine", 3)
    ]

    for s in students:
        print(f"Type: {type(s).__name__}")
        print(s.to_string())
        print()

def scenario_2():
    print_separator("2: polyform func")

    objects = [
    BachelorStudent("bayle bachelor", 19, 'hopital', 1, "Programming"),
    MasterStudent("michael masters", 23, 'hopital', 2, "AI"),
    PhDStudent("Gregory House, M.D.", 45, 'hopital', 3, "Medicine", 3),
        "just a string"
    ]

    printable = [obj for obj in objects if isinstance(obj, Printable)]
    print("only Printable:")
    print_all_printable(printable)

    print("\ncheck via isinstance:")
    for obj in objects[:3]:
        print(f"{obj.student_name}: Printable? {isinstance(obj, Printable)}, Comparable? {isinstance(obj, Comparable)}")

def scenario_3():
    print_separator("3: collection and filters")

    group = StudentGroup("hopital")

    group.add(BachelorStudent("bayle bachelor", 19, 'hopital', 1, "Programming", True))
    group.add(MasterStudent("michael masters", 23, 'hopital', 2, "AI", False, True))
    group.add(PhDStudent("Gregory House, M.D.", 45, 'hopital', 3, "Medicine", 3))

    print("Исходная коллекция:")
    print(group)
    
    printable_coll = StudentGroup(group.name)
    for item in group:
        if isinstance(item, Printable):
            printable_coll.add(item)
    
    print("\Only Printable:")
    print(printable_coll)

    print("\nSorting via GPA (Comparable):")
    group.sort_by_gpa()
    print(group)

    s1 = BachelorStudent("s1", 23, 'sduasd', 3, "Programming")
    s1.grade(5)
    s2 = BachelorStudent("s2", 19, 'hopital', 1, "Programming")
    s2.grade(4)
    cmp = s1.compare_to(s2)
    print(f"\ns1.compare_to(s2) = {cmp} ({'less' if cmp < 0 else 'more' if cmp > 0 else 'equal'})")

if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()