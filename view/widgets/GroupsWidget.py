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

        self.tab_layout_groups = QGridLayout()  # Основной макет
        self.tab_group = QGroupBox(name)  # Основной виджет

        self.content_widget = QStackedWidget()  # Этот виджет будет управлять отображением контента
        self.grid = QGridLayout()

        self.grid.addWidget(self.tab_group, 0, 0)
        self.tab_group.setLayout(self.tab_layout_groups)
        self.setLayout(self.grid)
        self.grid.addWidget(self.content_widget, 0, 1)

        self.init_ui()

    def init_ui(self):
        try:
            for index, _id in enumerate(self.groups):
                group: Group = self.group_repository.find_by_id(_id)

                # Создаем виджет с предметами для группы и передаем основной GridLayout
                lessons_widget = LessonsWidget(f"Предметы - {group.name}", group.lessons, self.grid)
                self.content_widget.addWidget(lessons_widget)

                button_group = QPushButton(group.name)

                # Используем замыкание, чтобы сохранить текущий индекс
                button_group.clicked.connect(lambda _, idx=index: self.show_content(idx))

                self.tab_layout_groups.addWidget(button_group)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_type, exc_value, exc_traceback)

    def show_content(self, index):
        print(f"Switching to index {index}")
        self.content_widget.setCurrentIndex(index)

