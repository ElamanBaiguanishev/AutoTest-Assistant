import sys

from PyQt5.QtWidgets import QTabWidget

from api.repositories.semestr_repository import SemestrRepository
from view.widgets.GroupsWidget import GroupsWidget
from view.widgets.LessonsWidget import LessonsWidget


class SemestrTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.semestr_repository = SemestrRepository()
        print(self.semestr_repository.get_all())
        self.init_ui()

    def init_ui(self):
        try:
            for semestr in self.semestr_repository.get_all():
                tab = GroupsWidget(f"Группы {semestr.name}", semestr.groups)
                self.addTab(tab, semestr.name)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_type, exc_value, exc_traceback, e)
