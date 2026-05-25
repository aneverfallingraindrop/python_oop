from app import StudentApp, StudentType
from exceptions import AppError

class CLI:
    def __init__(self, app: StudentApp) -> None:
        self._app = app
        self._is_running = True

    def run(self) -> None:
        while self._is_running:
            self._print_menu()
            raw_choice = input("Выберите пункт: ").strip()
            try:
                choice = int(raw_choice)
            except ValueError:
                print("Ошибка: введите число.")
                continue

            try:
                self._handle_choice(choice)
            except AppError as exc:
                print(f"Ошибка: {exc}")
            except ValueError as exc:
                print(f"Ошибка: {exc}")

    def _print_menu(self) -> None:
        print("\n\n1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента по имени")
        print("4. Фильтрация")
        print("5. Сортировка")
        print("6. Удалить студента")
        print("0. Выход")

    def _handle_choice(self, choice: int) -> None:
        if choice == 1:
            self._add_student()
        elif choice == 2:
            self._show_students(self._app.list_students())
        elif choice == 3:
            self._find_student()
        elif choice == 4:
            self._filter_students()
        elif choice == 5:
            self._sort_students()
        elif choice == 6:
            self._delete_student()
        elif choice == 0:
            self._app.save_data()
            self._is_running = False
            print("Данные сохранены. Завершение работы.")
        else:
            print("Ошибка: неверный пункт меню.")

    def _add_student(self) -> None:
        print("\nТип студента:")
        print("1. Student")
        print("2. BachelorStudent")
        print("3. MasterStudent")
        print("4. PhDStudent")

        type_choice = self._read_int("Выберите тип: ")
        type_map = {
            1: "student",
            2: "bachelor",
            3: "master",
            4: "phd",
        }
        if type_choice not in type_map:
            raise ValueError("Неверный тип студента.")

        name = input("Имя: ").strip()
        age = self._read_int("Возраст: ")
        group_prompt = f"Группа [{self._app.group_name}]: "
        group = input(group_prompt).strip() or self._app.group_name
        course = self._read_int("Курс (1-6): ")
        gpa = self._read_float("GPA: ")

        specialization = ""
        research_topic = ""
        has_practice = False
        has_thesis = False
        publications = 0

        if type_choice == 2:
            specialization = input("Специальность: ").strip()
            has_practice = self._confirm("Практика завершена? (y/n): ")
        elif type_choice == 3:
            research_topic = input("Тема исследования: ").strip()
            has_thesis = self._confirm("Диссертация защищена? (y/n): ")
        elif type_choice == 4:
            research_topic = input("Научная область: ").strip()
            publications = self._read_int("Количество публикаций: ")

        student = self._app.add_student(
            student_type=type_map[type_choice],
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
        print(f"Добавлен: {student.student_name}")

    def _find_student(self) -> None:
        name = input("Введите имя для поиска: ").strip()
        student = self._app.find_student_by_name(name)
        self._show_students([student])

    def _filter_students(self) -> None:
        print("\nФильтрация:")
        print("1. По курсу")
        print("2. По минимальному GPA")
        choice = self._read_int("Выберите фильтр: ")

        if choice == 1:
            course = self._read_int("Курс: ")
            students = self._app.filter_students_by_course(course)
        elif choice == 2:
            min_gpa = self._read_float("Минимальный GPA: ")
            students = self._app.filter_students_by_min_gpa(min_gpa)
        else:
            raise ValueError("Неверный пункт фильтрации.")

        self._show_students(students)

    def _sort_students(self) -> None:
        print("\nСортировать по:")
        print("1. Имени")
        print("2. GPA")
        print("3. Курсу")
        choice = self._read_int("Выберите стратегию: ")

        strategy_map = {
            1: "name",
            2: "gpa",
            3: "course",
        }
        if choice not in strategy_map:
            raise ValueError("Неверная стратегия сортировки.")

        reverse = self._confirm("Обратный порядок? (y/n): ")
        students = self._app.sort_students(strategy_map[choice], reverse=reverse)
        self._show_students(students)

    def _delete_student(self) -> None:
        name = input("Введите имя для удаления: ").strip()
        student = self._app.find_student_by_name(name)
        if not self._confirm(f'Удалить "{student.student_name}"? (y/n): '):
            print("Удаление отменено.")
            return
        removed = self._app.remove_student_by_name(name)
        print(f"Удален: {removed.student_name}")

    def _show_students(self, students: list[StudentType]) -> None:
        if not students:
            print("Коллекция пуста.")
            return

        headers = ["#", "Тип", "Имя", "Возраст", "Группа", "Курс", "GPA", "Детали"]
        rows: list[list[str]] = []

        for index, student in enumerate(students, start=1):
            rows.append(
                [
                    str(index),
                    type(student).__name__,
                    student.student_name,
                    str(student.student_age),
                    student.student_group,
                    str(student.student_course),
                    f"{student.student_gpa:.2f}",
                    self._student_details(student),
                ]
            )

        widths = [len(header) for header in headers]
        for row in rows:
            for column_index, value in enumerate(row):
                widths[column_index] = max(widths[column_index], len(value))

        header_line = " | ".join(text.ljust(widths[i]) for i, text in enumerate(headers))
        separator_line = "-+-".join("-" * width for width in widths)
        print(header_line)
        print(separator_line)
        for row in rows:
            print(" | ".join(value.ljust(widths[i]) for i, value in enumerate(row)))

    def _student_details(self, student: StudentType) -> str:
        if hasattr(student, "specialty"):
            return f"Специальность: {student.specialization}, Практика: {student.has_practice}" #type: ignore
        if hasattr(student, "research_topic"):
            return f"Тема: {student.research_topic}, Диссертация: {student.has_thesis}" #type: ignore
        if hasattr(student, "research_area"):
            return f"Область: {student.research_area}, Публикации: {student.publications}" #type: ignore
        return "Базовый студент"

    def _read_int(self, prompt: str) -> int:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError as exc:
            raise ValueError("Введите целое число.") from exc

    def _read_float(self, prompt: str) -> float:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError as exc:
            raise ValueError("Введите число.") from exc

    def _confirm(self, prompt: str) -> bool:
        answer = input(prompt).strip().lower()
        return answer in {"y", "yes", "д", "да"}

