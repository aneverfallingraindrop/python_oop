import os
import sys

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.lab01.model import Student
from src.lab03.models import BachelorStudent, MasterStudent, PhDStudent
from src.lab05.collection import StudentGroup

from exceptions import DuplicateItemError, InvalidStudentTypeError, ItemNotFoundError
from storage import load, save

StudentType = Student | BachelorStudent | MasterStudent | PhDStudent


class StudentApp:

    def __init__(
        self,
        group_name: str,
        data_file: str | None = None,
        auto_load: bool = True,
    ) -> None:
        default_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")
        self._data_file = data_file or default_data_file
        self._group = StudentGroup(group_name)
        if auto_load:
            self.load_data()

    @property
    def group_name(self) -> str:
        return self._group.name

    def add_student(
        self,
        student_type: str,
        name: str,
        age: int,
        group: str,
        course: int,
        gpa: float,
        specialization: str = "",
        research_topic: str = "",
        has_practice: bool = False,
        has_thesis: bool = False,
        publications: int = 0,
    ) -> StudentType:
        student = self._build_student(
            student_type=student_type,
            name=name,
            age=age,
            group=group,
            course=course,
            gpa=gpa,
            specialization=specialization,
            research_topic=research_topic,
            has_practice=has_practice,
            has_thesis=has_thesis,
            publications=publications,
        )

        try:
            self._group.add(student)
        except ValueError as exc:
            message = str(exc).lower()
            if "already present" in message:
                raise DuplicateItemError("Student already present in collection.") from exc
            raise
        return student

    def list_students(self) -> list[StudentType]:
        return self._group.get_all()

    def find_student_by_name(self, name: str) -> StudentType:
        student = self._group.find_by_name(name.strip())
        if student is None:
            raise ItemNotFoundError(f"Студент '{name}' не найден.")
        return student

    def remove_student_by_name(self, name: str) -> StudentType:
        student = self.find_student_by_name(name)
        try:
            self._group.remove(student)
        except ValueError as exc:
            raise ItemNotFoundError(f"Студент '{name}' не найден.") from exc
        return student

    def filter_students_by_course(self, course: int) -> list[StudentType]:
        return list(filter(lambda student: student.student_course == course, self._group))

    def filter_students_by_min_gpa(self, min_gpa: float) -> list[StudentType]:
        return list(filter(lambda student: student.student_gpa >= min_gpa, self._group))

    def sort_students(self, strategy: str, reverse: bool = False) -> list[StudentType]:
        strategy_key = strategy.strip().lower()
        if strategy_key == "name":
            self._group.sort_by_name(reverse=reverse)
        elif strategy_key == "gpa":
            self._group.sort_by_gpa(reverse=reverse)
        elif strategy_key == "course":
            self._group.sort_by_course(reverse=reverse)
        else:
            raise ValueError("Неизвестная стратегия сортировки.")
        return self.list_students()

    def load_data(self) -> None:
        self._group = load(self._data_file, self._group.name)

    def save_data(self) -> None:
        save(self._group, self._data_file)

    def _build_student(
        self,
        student_type: str,
        name: str,
        age: int,
        group: str,
        course: int,
        gpa: float,
        specialization: str,
        research_topic: str,
        has_practice: bool,
        has_thesis: bool,
        publications: int,
    ) -> StudentType:
        normalized_type = student_type.strip().lower()
        if normalized_type == "student":
            return Student(name, age, group, course, gpa)
        if normalized_type == "bachelor":
            return BachelorStudent(name, age, group, course, specialization, has_practice, gpa)
        if normalized_type == "master":
            return MasterStudent(name, age, group, course, research_topic, has_thesis, False, gpa)
        if normalized_type == "phd":
            return PhDStudent(name, age, group, course, research_topic, publications, False, gpa)
        raise InvalidStudentTypeError("Неизвестный тип студента.")

