import json
import os
import pandas as pd
import uuid

from api.models.Group import Group
from api.models.Lesson import Lesson
from api.models.Semestr import Semestr
from api.models import Student
from api.models.Test import Test
from api.repositories.semestr_repository import SemestrRepository
from api.repositories import GroupRepository
from api.repositories.lesson_repository import LessonRepository
from api.repositories.test_repository import TestRepository
from api.repositories.student_repository import StudentRepository

config_path = "resources/db.json"


def check_config() -> bool:
    try:
        if os.path.getsize(config_path) == 0:
            return False
        else:
            return True
    except FileNotFoundError:
        return False


def data(command) -> None:
    if command:
        with open("resources/path.json") as json_file:
            data_json = json.load(json_file)
            path = data_json["db"]

        semestr_repository = SemestrRepository()
        group_repository = GroupRepository()
        lesson_repository = LessonRepository()
        test_repository = TestRepository()
        student_repository = StudentRepository()

        dirs = os.listdir(path)

        def generate_students(path_group) -> dict:
            df = pd.read_excel(path_group + "/Студенты.xlsx", header=None, skiprows=1, usecols=[0, 1, 2])
            students = {}

            for _, row in df.iterrows():
                my_uuid: str = str(uuid.uuid4())
                student = Student(id=my_uuid, fio=row[0], login=row[1], password=row[2])
                student_repository.add(student)
                students[my_uuid] = student

            return students

        def generate_lessons(path_group) -> dict:
            excel_file = pd.ExcelFile(path_group + "/Предметы.xlsx")
            lessons = {}

            for sheet_name in excel_file.sheet_names:
                lesson_id = str(uuid.uuid4())
                lesson = Lesson(id=lesson_id, name=sheet_name, tests=[])

                for _, row in pd.read_excel(excel_file, sheet_name).iterrows():
                    test_id = str(uuid.uuid4())
                    test = Test(id=test_id, name=row[0], urls=[row[1]])
                    lesson.tests.append(test_id)
                    test_repository.add(test)

                lesson_repository.add(lesson)
                lessons[lesson_id] = lesson

            return lessons

        for index, dir_ in enumerate(dirs):
            # progress_value = (index + 1) / len(dirs) * 100
            # progress_callback(progress_value)

            semestr_id = str(uuid.uuid4())
            semestr = Semestr(id=semestr_id, name=dir_, groups=[])

            for folder_group in os.listdir(os.path.join(path, dir_)):
                group_id = str(uuid.uuid4())
                group = Group(id=group_id, name=folder_group, students=[], lessons=[])

                group.students = list(generate_students(os.path.join(path, dir_, folder_group)).keys())
                group.lessons = list(generate_lessons(os.path.join(path, dir_, folder_group)).keys())

                group_repository.add(group)
                semestr.groups.append(group_id)

            semestr_repository.add(semestr)

        # Удаляем старый конфиг файл, если он существует
        if os.path.exists(config_path):
            os.remove(config_path)

        print("Data successfully imported and saved in respective repositories.")
    else:
        # Если данные уже есть, можно добавить код для загрузки и отображения данных, если требуется
        pass


data(True)
