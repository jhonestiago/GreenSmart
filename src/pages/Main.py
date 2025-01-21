import sys

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon

class Main(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.__init_components()
        self.__error_color = 'background-color: rgb(204, 41, 54); color: rgb(255, 255, 255);'
        self.__sucess_color = 'background-color: rgb(101, 184, 145);'

    def __init_components(self) -> None:
        #pageLogin
        self.frameLoginMessages.hide()
        self.pushButtonLoginEnter.clicked.connect(self.__enter)
        self.pushButtonLoginRegister.clicked.connect(self.__pageRegistration)
        self.pushButtonLoginCloseMessage.clicked.connect(self.frameLoginMessages.hide)

        #pageSystem
        self.pushButtonSystemForm.setIcon(QIcon('src/img/form.png'))
        self.pushButtonSystemDatabase.setIcon(QIcon('src/img/database.png'))
        self.pushButtonSystemUsers.setIcon(QIcon('src/img/user.png'))
        self.pushButtonSystemSettings.setIcon(QIcon('src/img/settings.png'))

        #.pageForm

    def __enter(self) -> None:
        username = self.lineEditLoginUsername.text()
        password = self.lineEditLoginPassword.text()
        if username == "admin" and  password == "12345":
            self.lineEditLoginUsername.clear()
            self.lineEditLoginPassword.clear()
            self.frameLoginMessages.hide()
            self.__pageForm()
        else:
            message = 'Usuário ou Senha incorretos'
            self.labelLoginMessage.setText(message)
            self.labelLoginMessage.setStyleSheet(self.__error_color)
            self.frameLoginMessages.show()


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
