import sys

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class Main(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.__init_components()

    def __init_components(self) -> None:
        #pageLogin
        self.frameLoginMessages.hide()
        self.pushButtonLoginEnter.clicked.connect(self.__enter)
        self.pushButtonLoginRegister.clicked.connect(self.__pageRegistration)
        self.pushButtonLoginCloseMessage.clicked.connect(self.frameLoginMessages.hide)

    def __enter(self) -> None:
        pass

    def __pageLogin(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageLogin)

    def __pageForm(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageForm)

    def __pageDatabase(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageDatabase)

    def __pageUsers(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageUsers)

    def __pageSettings(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageSettings)

    def __pageRegistration(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageRegistration)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    main = Main()
    main.setWindowTitle('GreenSmart')
    main.show()
    qt.exec()
