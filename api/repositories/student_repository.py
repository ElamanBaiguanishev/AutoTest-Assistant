from typing import List, Optional

from api.models.Student import Student, student_id
from api.repositories.base_repository import BaseRepository
from view.utils.file_manager import FileManager


class StudentRepository(BaseRepository[Student, student_id]):
    def __init__(self):
        self.file_manager = FileManager('resources/db/students.json')

    def get_all(self) -> List[Student]:
        return self.file_manager.load_data(Student)

    def find_by_id(self, _id: student_id) -> Optional[Student]:
        students = self.file_manager.load_data(Student)
        return next((student for student in students if student.id == _id), None)

    def add(self, student: Student):
        students = self.file_manager.load_data(Student)
        students.append(student)
        self.file_manager.save_data(students)

    def update(self, _id: student_id, updated_student: Student):
        students = self.file_manager.load_data(Student)
        for index, student in enumerate(students):
            if student.id == _id:
                students[index] = updated_student
                break
        self.file_manager.save_data(students)

    def delete(self, _id: student_id):
        students = self.file_manager.load_data(Student)
        students = [student for student in students if student.id != _id]
        self.file_manager.save_data(students)
