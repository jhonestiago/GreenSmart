import numpy as np

class User:
    'Cria a classe User'

    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__email = None
        self.__username = None
        self.__password_1 = None
        self.__password_2 = None
        self.__messages = np.zeros(6, dtype=object)

    @property
    def first_name(self) -> str:
        '''
        Retorna o primeiro nome do usuário.'
        '''
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name:str) -> None:
        '''
        Altera o primeiro nome do usuário
        '''
        if len(first_name) != 0:
            self.__first_name = first_name
            self.__messages[0] = 0
        else:
            message = 'campo obrigatório'
            self.__messages[0] = message

    @property
    def last_name(self) -> str:
        '''
        Retorna o sobrenome do usuário.
        '''
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name:str) -> None:
        '''
        Altera o sobrenome do usuário.
        '''
        if len(last_name) != 0:
            self.__last_name = last_name
            self.__messages[1] = 0
        else:
            message = 'campo obrigatório'
            self.__messages[1] = message

    @property
    def email(self) -> str:
        '''
        Retorna o email do usuário
        '''
        return self.__email

    @email.setter
    def email(self, email:str) -> None:
        '''
        Altera o email do usuário
        '''
        if len(email) != 0:
            self.__email = email
            self.__messages[2] = 0
        else:
            message = 'campo obrigatório'
            self.__messages[2] = message

    @property
    def username(self) -> str:
        '''
        Retorna o nome de usuário.
        '''
        return self.__username

    @username.setter
    def username(self, username:str) -> None:
        '''
        Altera o nome de usuário
        '''
        if len(username) != 0:
            self.__username = username
            self.__messages[3] = 0
        else:
            message = 'campo obrigatório'
            self.__messages[3] = message

    @property
    def password_1(self) -> str:
        '''
        Retorna a senha principal do usuário.
        '''
        return self.__password_1

    @password_1.setter
    def password_1(self, password:str) -> None:
        '''
        Altera a senha principal do usuário
        '''
        if len(password) != 0:
            if len(password) >= 5 and len(password) <= 8:
                self.__password_1 = password
                self.__messages[4] = 0
            else:
                message = 'a senha deve ter 5 e 8 caracteres'
                self.__messages[4] = message
        else:
            message = 'campo obrigatório'
            self.__messages[4] = message

    @property
    def password_2(self) -> str:
        '''
        Retorna a confirmação da senha.
        '''
        return self.__password_2

    @password_2.setter
    def password_2(self, password:str) -> None:
        '''
        Altera a confirmação da senha
        '''
        if len(password) != 0:
            if password == self.__password_1:
                self.__password_2 = password
                self.__messages[5] = 0
            else:
                message = 'As senhas não coincidem'
                self.__messages[5] = message
        else:
            message = 'campo obrigatório'
            self.__messages[5] = message

    @property
    def messages(self) -> list:
        '''
        Retorna uma lista com mensagens
        '''
        return self.__messages

    @messages.setter
    def messages(self, messages:list) -> None:
        pass
