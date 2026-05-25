import os

from app import StudentApp
from cli import CLI
from exceptions import StorageError


def main() -> None:
    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")
    try:
        app = StudentApp(group_name="BIVT-25-8", data_file=data_file, auto_load=True)
    except StorageError as exc:
        print(f"Ошибка загрузки данных: {exc}")
        app = StudentApp(group_name="BIVT-25-8", data_file=data_file, auto_load=False)

    cli = CLI(app)
    cli.run()


if __name__ == "__main__":
    main()

