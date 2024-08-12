import sys
import textwrap

from PyQt5.QtWidgets import QStackedWidget, QGroupBox, QVBoxLayout, QPushButton, QWidget

from api.models.Lesson import Lesson
from api.repositories.lesson_repository import LessonRepository
from view.widgets.TestsWidget import TestWidget


class LessonsWidget(QGroupBox):
    def __init__(self, name, lessons, grid):
        super().__init__(name)

        self.lesson_repository = LessonRepository()
        self.lessons = lessons
        self.grid = grid  # Передаем основной GridLayout

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.init_ui()

    def init_ui(self):
        try:
            for index, _id in enumerate(self.lessons):
                lesson: Lesson = self.lesson_repository.find_by_id(_id)

                button_lesson = QPushButton(lesson.name)
                button_lesson.clicked.connect(lambda _, l=lesson: self.show_tests(l))

                self.main_layout.addWidget(button_lesson)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_type, exc_value, exc_traceback)

    def show_tests(self, lesson):
        print(f"Showing tests for lesson {lesson.name}")

        # Удаляем старый виджет с тестами, если он существует
        # if hasattr(self, 'test_widget'):
        #     self.grid.removeWidget(self.test_widget)
        #     self.test_widget.deleteLater()

        # Создаем новый виджет с тестами и добавляем его на третью позицию в GridLayout
        self.test_widget = TestWidget(lesson.name, lesson.tests)
        self.grid.addWidget(self.test_widget, 0, 2)
