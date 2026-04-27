import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *
from src.lab02.collection import *
from src.lab03.models import *

def print_separator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)


def demo():

    print_separator("1. creating child classes")
    
    bachelor = BachelorStudent("bayle bachelor", 19, 'hopital', 1, "Programming")
    master = MasterStudent("michael masters", 23, 'hopital', 2, "AI")
    phd = PhDStudent("Gregory House, M.D.", 45, 'hopital', 3, "Medicine", 3)
    
    print("Bachelor:")
    print(bachelor)
    print("\nMaster:")
    print(master)
    print("\nDoctor:")
    print(phd)

    print_separator("2. unique methods of child classes")
    
    print(bachelor.complete_practice())
    print(master.defend_thesis())
    print(phd.publish_article())
 
    print_separator("3. polymorphism — grant_scholarship()")
    
    students = [bachelor, master, phd]
    for s in students:
        print(f"{s.student_name} ({type(s).__name__}): scholarship? {s.grant_scholarship()}")

    print_separator("4. redefine upgrade_course()")
    
    bachelor_4 = BachelorStudent("filler", 20, 'filler', 4, "filler")
    print(f"bachelor on 4th course: {bachelor_4.student_name}")
    try:
        bachelor_4.upgrade_course()
    except Exception as e:
        print(f"  Ошибка: {e}")

    print_separator("5. mixed StudentGroup")
    
    group = StudentGroup("hopital")
    group.add(bachelor)
    group.add(master)
    group.add(phd)
    
    print(group)
 
    print_separator("6. isinstance")
    
    print("bachelors:")
    for s in group:
        if isinstance(s, BachelorStudent):
            print(f"  - {s.student_name} ({s.specialization})")
    
    print("\nmasters:")
    for s in group:
        if isinstance(s, MasterStudent):
            print(f"  - {s.student_name} ({s.research_topic})")
    
    print("\ndoctors:")
    for s in group:
        if isinstance(s, PhDStudent):
            print(f"  - {s.student_name} ({s.research_area}, публикаций: {s.publications})")

    print_separator("7. polymorphism in collection")
    
    print("diff. scholarships based on type:")
    for s in group:
        print(f"  {s.student_name} ({type(s).__name__}): {s.grant_scholarship()}")

    print_separator("8. typecheck")
    
    print(f"bayle — bachelor? {isinstance(bachelor, BachelorStudent)}")
    print(f"bayle — student? {isinstance(bachelor, Student)}")
    print(f"bayle — master? {isinstance(bachelor, MasterStudent)}")
    print(f"michael — student? {isinstance(master, Student)}")

    print_separator("9. grant_scholarship() comparisons")
    
    print("При одинаковой оценке 4.5:")
    test_bachelor = BachelorStudent("bachelor", 19, 'hopital', 1, "Programming")
    test_master = MasterStudent("master", 23, 'hopital', 2, "AI")
    test_phd = PhDStudent("house", 45, 'hopital', 3, "Medicine", 3)

    test_bachelor.grade(4)
    test_bachelor.grade(3)
    test_master.grade(4)
    test_master.grade(5)
    test_phd.grade(4)
    test_phd.grade(5)
    
    print(f"  Bachelor (GPA 4.5): {test_bachelor.grant_scholarship()}")
    print(f"  Master (GPA 4.5): {test_master.grant_scholarship()} (needed >4.2)")
    print(f"  Doctor (GPA 4.5): {test_phd.grant_scholarship()} (always)")


if __name__ == "__main__":
    demo()