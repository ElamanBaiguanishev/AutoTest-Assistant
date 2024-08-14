import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QPushButton, QGroupBox, QStackedWidget

from api.models.Group import group_id, Group
from api.repositories.group_repository import GroupRepository
from view.widgets.LessonsWidget import LessonsWidget


class GroupsWidget(QWidget):
    def __init__(self, name, groups: list[group_id]):
        super().__init__()
        self.groups = groups
        self.group_repository = GroupRepository()

        self.semestr_content_layout = QGridLayout()  # Основной макет (в нем 3 groupbox)

        self.tab_group = QGroupBox(name)  # Основной виджет

        self.semestr_group_layout = QGridLayout()

        self.semestr_content_layout.addWidget(self.tab_group, 0, 0)

        self.tab_group.setLayout(self.semestr_group_layout)

        self.setLayout(self.semestr_content_layout)

        self.init_ui()

    def init_ui(self):
        try:
            for _id in self.groups:
                group: Group = self.group_repository.find_by_id(_id)

                button_group = QPushButton(group.name)

                # Используем замыкание, чтобы сохранить текущий индекс
                button_group.clicked.connect(lambda _, g=group: self.create_lessons(g))

                self.semestr_group_layout.addWidget(button_group)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_type, exc_value, exc_traceback)

    def create_lessons(self, group):
        lessons_widget = LessonsWidget(f"Предметы - {group.name}", group.lessons, self.semestr_content_layout)
        self.semestr_content_layout.addWidget(lessons_widget, 0, 1)
