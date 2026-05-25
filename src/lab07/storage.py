import json
import os
import sys
from typing import Any

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.lab01.model import Student
from src.lab03.models import BachelorStudent, MasterStudent, PhDStudent
from src.lab05.collection import StudentGroup

from exceptions import StorageError

StudentType = Student | BachelorStudent | MasterStudent | PhDStudent


def save(collection: StudentGroup, filepath: str) -> None:
    payload = {
        "group_name": collection.name,
        "students": [_student_to_dict(student) for student in collection.get_all()],
    }

    try:
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
    except (OSError, TypeError, ValueError) as exc:
        raise StorageError(f"Не удалось сохранить данные: {exc}") from exc


def load(filepath: str, default_group_name: str) -> StudentGroup:
    if not os.path.exists(filepath):
        return StudentGroup(default_group_name)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            payload = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise StorageError(f"Не удалось загрузить данные: {exc}") from exc

    if not isinstance(payload, dict):
        raise StorageError("Некорректный формат файла: ожидается JSON-объект.")

    group_name = str(payload.get("group_name", default_group_name))
    raw_students = payload.get("students", [])
    if not isinstance(raw_students, list):
        raise StorageError("Некорректный формат файла: поле students должно быть списком.")

    group = StudentGroup(group_name)
    for item in raw_students:
        if not isinstance(item, dict):
            raise StorageError("Некорректный формат записи студента.")
        student = _student_from_dict(item)
        try:
            group.add(student)
        except ValueError as exc:
            raise StorageError(f"Ошибка при загрузке студента: {exc}") from exc
    return group


def _student_to_dict(student: StudentType) -> dict[str, Any]:
    data: dict[str, Any] = {
        "type": type(student).__name__,
        "name": student.student_name,
        "age": student.student_age,
        "group": student.student_group,
        "course": student.student_course,
        "gpa": student.student_gpa,
        "active": student.active,
    }

    if isinstance(student, BachelorStudent):
        data["specialization"] = student.specialization
        data["has_practice"] = student.has_practice
    elif isinstance(student, MasterStudent):
        data["research_topic"] = student.research_topic
        data["has_thesis"] = student.has_thesis
    elif isinstance(student, PhDStudent):
        data["research_area"] = student.research_area
        data["publications"] = student.publications
    return data


def _student_from_dict(data: dict[str, Any]) -> StudentType:
    student_type = str(data.get("type", "Student"))
    name = str(data["name"])
    age = int(data["age"])
    group = str(data["group"])
    course = int(data["course"])
    gpa = float(data.get("gpa", 0.0))

    if student_type == "BachelorStudent":
        student: StudentType = BachelorStudent(
            name,
            age,
            group,
            course,
            str(data.get("specialization", "")),
            bool(data.get("has_practice", False)),
            gpa,
        )
    elif student_type == "MasterStudent":
        student = MasterStudent(
            name,
            age,
            group,
            course,
            str(data.get("research_topic", "")),
            bool(data.get("has_thesis", False)),
            False,
            gpa,
        )
    elif student_type == "PhDStudent":
        student = PhDStudent(
            name,
            age,
            group,
            course,
            str(data.get("research_area", "")),
            int(data.get("publications", 0)),
            False,
            gpa,
        )
    else:
        student = Student(name, age, group, course, gpa)

    student.active = bool(data.get("active", True))
    return student

