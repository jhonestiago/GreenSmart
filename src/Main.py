import sys

from MainGUI import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication 
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QIcon

from models.User import User

from controllers.UserControl import UserControl

class Main(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.__init_components()
        self.__init_controllers()
        self.__init_users()
        self.__init_style()
        self.__flag = False
    
    def __init_components(self) -> None:
        #pageLogin
        self.frameLoginMessages.hide()
        self.pushButtonLoginEnter.clicked.connect(self.__enter)
        self.pushButtonLoginRegister.clicked.connect(self.__pageRegistration)
        self.pushButtonLoginCloseMessage.clicked.connect(self.frameLoginMessages.hide)

        #pageSystem
        self.frameSystemMessage.hide()
        self.pushButtonSystemForm.setIcon(QIcon('src/img/form.png'))
        self.pushButtonSystemDatabase.setIcon(QIcon('src/img/database.png'))
        self.pushButtonSystemUsers.setIcon(QIcon('src/img/user.png'))
        self.pushButtonSystemSettings.setIcon(QIcon('src/img/settings.png'))
        self.pushButtonSystemExit.setIcon(QIcon('src/img/exit.png'))
        self.pushButtonSystemForm.clicked.connect(self.__pageForm)
        self.pushButtonSystemDatabase.clicked.connect(self.__pageDatabase)
        self.pushButtonSystemUsers.clicked.connect(self.__pageUsers)
        self.pushButtonSystemSettings.clicked.connect(self.__pageSettings)
        self.pushButtonSystemExit.clicked.connect(self.__pageLogin)
        self.pushButtonSystemCloseMessage.clicked.connect(self.frameSystemMessage.hide)

        #.pageForm
        #self.pushButtonFormRegister.clicked.connect()

        #.pageDatabase
        #self.pushButtonDatabaseEdit.clicked.connect()
        #self.pushButtonDatabaseDelete.clicked.connect()
        #self.pushButtonDatabaseEditClients.clicked.connect()
        #self.pushButtonDatabaseDeleteClients.clicked.connect()

        #.pageUsers
        #self.pushButtonUsersDelete.clicked.connect()

        #.pageSettings
        #self.pushButtonSettingsSaveData.clicked.connect()
        #self.pushButtonSettingsSavePassword.clicked.connect()

        #pageRegistration
        self.frameRegistrationMessage.hide()
        self.pushButtonRegistrationSave.clicked.connect(self.__register_user)
        self.pushButtonRegistrationBack.clicked.connect(self.__pageLogin)
        self.pushButtonRegistrationCloseMessage.clicked.connect(self.frameRegistrationMessage.hide)

    def __init_style(self) -> None:
        self.__error_color = 'background-color: rgb(204, 41, 54); color: rgb(255, 255, 255);'
        self.__sucess_color = 'background-color: rgb(101, 184, 145);'
        self.__error_border = 'border: 2px solid rgb(255, 0, 0);'
    
    def __init_controllers(self) -> None:
        self.__user_control = UserControl()

    def __init_users(self) -> None:
        '''
        Inicializa o usuario admin
        '''
        admin = User()
        admin.first_name = 'admin'
        admin.username = 'admin'
        admin.password_1 = '12345'
        admin.password_2 = '12345'
        self.__user_control.add_user(admin)

    def __enter(self) -> None:
        username = self.lineEditLoginUsername.text()
        password = self.lineEditLoginPassword.text()
        if self.__user_control.find_user(username, password):
            if username == 'admin':
                self.lineEditLoginUsername.clear()
                self.lineEditLoginPassword.clear()
                self.frameLoginMessages.hide()
                self.__flag = True
                self.__pageForm()
            else:
                self.lineEditLoginUsername.clear()
                self.lineEditLoginPassword.clear()
                self.frameLoginMessages.hide()
                self.__flag = False
                self.__pageForm()
        else:
            message = 'Usuário ou Senha incorretos'
            self.labelLoginMessage.setText(message)
            self.labelLoginMessage.setStyleSheet(self.__error_color)
            self.frameLoginMessages.show()


    # Novos Usuários
    def __register_user(self) -> None:
        inputs = self.__registation_inputs()
        counter = 0

        user = User()
        user.first_name = inputs[0].text()
        user.last_name = inputs[1].text()
        user.email = inputs[2].text()
        user.username = inputs[3].text()
        user.password_1 = inputs[4].text()
        user.password_2 = inputs[5].text()

        for i, message in enumerate(user.messages):
            if message != 0:
                inputs[i-1].setPlaceholderText(message)
                inputs[i-1].setStyleSheet(self.__error_border)
                counter += 1

        if counter > 0:
            message = f'Há {counter} campo(s) a ser(em) preenchido(s)'
            self.labelRegistrationMessage.setText(message)
            self.labelRegistrationMessage.setStyleSheet(self.__error_color)
            self.frameRegistrationMessage.show()
        else:
            pass

    def __registation_inputs(self) -> list:
        inputs = [
            self.lineEditRegistrationFirstName,
            self.lineEditRegistrationLastName,
            self.lineEditRegistrationEmail,
            self.lineEditRegistrationUsername,
            self.lineEditRegistrationPassword1,
            self.lineEditRegistrationPassword2
        ]
        return inputs
        
    # Navegação

    def __pageLogin(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageLogin)

    def __pageForm(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageForm)

    def __pageDatabase(self) -> None:
        self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
        self.stackedWidgetSystem.setCurrentWidget(self.pageDatabase)

    def __pageUsers(self) -> None:
        if self.__flag:
            self.stackedWidgetMain.setCurrentWidget(self.pageSystem)
            self.stackedWidgetSystem.setCurrentWidget(self.pageUsers)
        else:
            message = 'Acesso negado'
            self.labelSystemMessage.setText(message)
            self.labelSystemMessage.setStyleSheet(self.__error_color)
            self.frameSystemMessage.show()

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
