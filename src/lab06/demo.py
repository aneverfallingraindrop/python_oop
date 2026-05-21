import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab03.models import *
from src.lab06.container import *

def print_separator(title: str = "") -> None:
    print(f"\n{'=' * 60}")
    if title:
        print(f" {title} ".center(60, '='))
    print(f"{'=' * 60}")


def create_students() -> list:
    return [
        BachelorStudent("joseph joestar", 19, "prog-2", 2, "Программирование", has_practice=True, gpa=4.5),
        BachelorStudent("jotaro kujo", 18, "prog-1", 1, "Экономика", gpa = 3.8),
        BachelorStudent("josuke higashikata", 20, "prog-3", 3, "Программирование", has_practice=True, gpa=4.9),
        BachelorStudent("giorno giovanna", 19, "econ-2", 2, "Экономика", gpa=3.2),
        MasterStudent("jolyne kujo", 21, "ai-4", 4, "Искусственный интеллект", gpa=4.7),
        BachelorStudent("johnny joestar", 18, "prog-1", 1, "Программирование", gpa = 4.1),
        MasterStudent("jodio joestar", 22, "bioinf-3", 3, "Биоинформатика", gpa=4.3),
    ]

def scenario_1() -> None:
    print_separator("1: type annotation")
    
    student: Student = BachelorStudent("johnny joestar", 21, "prog-2", 2, "Программирование")
    
    name: str = student.student_name
    age: int = student.student_age
    gpa: float = student.student_gpa
    
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Type name: {type(name).__name__}")
    print(f"Type age: {type(age).__name__}")
    print(f"Type GPA: {type(gpa).__name__}")


def scenario_2() -> None:
    print_separator("2: generic typedcollection")
    
    collection: TypedCollection[Student] = TypedCollection()
    
    students = create_students()
    
    print("adding students to the ocllection:")
    for s in students[:5]:
        collection.add(s)
        print(f"  added: {s.student_name}")
    
    print(f"\ncollection has {len(collection)} students")
    
    all_students = collection.get_all()
    print("\nAll students in collection:")
    for s in all_students:
        print(f"  - {s.student_name} (course {s.course}, gpa: {s.student_gpa:.2f})")

def scenario_3() -> None:
    print_separator("СЦЕНАРИЙ 3: find, filter, map")
    
    collection: TypedCollection[Student] = TypedCollection()
    for s in create_students():
        collection.add(s)

    print("--- find() ---")
    found = collection.find(lambda s: s.student_name == "jotaro kujo")
    if found:
        print(f"found: {found.student_name} (grade: {found.student_gpa})")
    
    not_found = collection.find(lambda s: s.student_name == "DIO")
    print(f"trying to find a nonexistent student: {not_found}")

    print("\n--- filter() ---")
    high_achievers = collection.filter(lambda s: s.student_gpa > 4.5)
    print(f"valedictorians (gpa > 4.5): {len(high_achievers)} students")
    for s in high_achievers:
        print(f"  - {s.student_name}: {s.student_gpa:.2f}")

    print("\n--- map() to names (str) ---")
    names: list[str] = collection.map(lambda s: s.student_name)
    print(f"names: {', '.join(names)}")
    print(f"result type: {type(names[0]).__name__ if names else 'empty'}")
    
    print("\n--- map() to gpa (float) ---")
    student_gpas: list[float] = collection.map(lambda s: s.student_gpa)
    print(f"GPAs: {student_gpas}")
    print(f"result type: {type(student_gpas[0]).__name__ if student_gpas else 'empty'}")
    
    print("\n--- map() to str (str) ---")
    info_list: list[str] = collection.map(lambda s: f"{s.student_name} (course {s.course})")
    for info in info_list[:5]:
        print(f"  {info}")

def scenario_4() -> None:
    print_separator("4: displayable")
    
    collection: TypedCollection[Displayable] = TypedCollection()
    
    students = create_students()
    collection.add(students[0])  
    collection.add(students[4])
    collection.add(students[6])  
    
    print("collection of Displayable objects:")
    print(f"Всего элементов: {len(collection)}")
    
    print("\ncalling str() for each:")
    for item in collection:
        print(f"  {str(item)}")

    print("\ndifferent types in one collection:")
    for item in collection:
        print(f"  Тип: {type(item).__name__}, display(): {str(item)}")

def scenario_5() -> None:
    print_separator("5: scoreable")

    collection: TypedCollection[Scorable] = TypedCollection()
    
    students = create_students()
    for s in students:
        collection.add(s)
    
    print(f"collection of scoreable objects (total: {len(collection)})")
    
    scores = [item.score() for item in collection]
    print(f"\ngrades of all students: {scores}")
    
    avg_score = sum(scores) / len(scores) if scores else 0
    print(f"average score: {avg_score:.2f}")
    
    high_scores = collection.filter(lambda s: s.score() > 4.5)
    print(f"\nstudents with score > 4.5: {len(high_scores)}")
    for s in high_scores:
        print(f"  - {s.score():.2f}")

if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()
    scenario_5()