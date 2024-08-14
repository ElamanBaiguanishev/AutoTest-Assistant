import sys
import textwrap

from PyQt5.QtWidgets import QStackedWidget, QGroupBox, QVBoxLayout, QPushButton, QWidget

from api.models.Test import Test
from api.repositories.test_repository import TestRepository


class TestWidget(QGroupBox):
    def __init__(self, name, tests):
        super().__init__(name)
        print(name)
        self.tests = tests
        self.test_repository = TestRepository()

        self.main_layout = QVBoxLayout()

        self.setLayout(self.main_layout)

        self.init_ui()

    def init_ui(self):
        try:
            for index, _id in enumerate(self.tests):
                test: Test = self.test_repository.find_by_id(_id)

                wrapped_text = "\n".join(textwrap.wrap(test.name, width=20))  # разбиваем текст на строки по 20 символов

                button_lesson = QPushButton(wrapped_text)

                self.main_layout.addWidget(button_lesson)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_type, exc_value, exc_traceback)
