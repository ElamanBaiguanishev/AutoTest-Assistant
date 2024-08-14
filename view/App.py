from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout

# from mock import mock
from view.widgets.SemestrTabWidget import SemestrTabWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.tab_widget = SemestrTabWidget()
        self.main_layout.addWidget(self.tab_widget, 1, 0)
        self.setLayout(self.main_layout)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(600, 200, 568, 500)
        self.setStyleSheet("background: #f7f7f7")
        icon = QIcon('resources/favicon.ico')
        self.setWindowIcon(icon)
        self.setStyleSheet(open("resources/styles.qss").read())
