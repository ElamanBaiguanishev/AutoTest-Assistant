import sys

from PyQt5.QtWidgets import QApplication

from view.App import App

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        # log_filename = create_log_file()
        # sys.excepthook = log_exception
        mainWindow = App()

        mainWindow.setStyleSheet(open("resources/styles.qss").read())
        mainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type, exc_value, exc_traceback)
        # log_exception(exc_type, exc_value, exc_traceback)
