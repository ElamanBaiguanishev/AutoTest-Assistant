from typing import List, Optional
from api.models.Lesson import Lesson, lesson_id
from api.repositories.base_repository import BaseRepository
from view.utils.file_manager import FileManager


class LessonRepository(BaseRepository[Lesson, lesson_id]):
    def __init__(self):
        self.file_manager = FileManager('resources/db/lessons.json')

    def get_all(self) -> List[Lesson]:
        return self.file_manager.load_data(Lesson)

    def find_by_id(self, _id: lesson_id) -> Optional[Lesson]:
        lessons = self.file_manager.load_data(Lesson)
        return next((lesson for lesson in lessons if lesson.id == _id), None)

    def add(self, lesson: Lesson):
        lessons = self.file_manager.load_data(Lesson)
        lessons.append(lesson)
        self.file_manager.save_data(lessons)

    def update(self, _id: lesson_id, updated_lesson: Lesson):
        lessons = self.file_manager.load_data(Lesson)
        for index, lesson in enumerate(lessons):
            if lesson.id == _id:
                lessons[index] = updated_lesson
                break
        self.file_manager.save_data(lessons)

    def delete(self, _id: lesson_id):
        lessons = self.file_manager.load_data(Lesson)
        lessons = [lesson for lesson in lessons if lesson.id != _id]
        self.file_manager.save_data(lessons)
