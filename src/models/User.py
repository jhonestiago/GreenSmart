import numpy as np

class User:
    '''
    Cria a classe User
    '''

    def __init__(self):
        self.__first_name:str = ''
        self.__last_name:str = ''
        self.__username:str = ''
        self.__password_1:str = ''
        self.__password_2:str = ''
        self.__error_message = np.zeros(5,dtype=object)

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name) -> None:
        if len(first_name) != 0:
            self.__first_name = first_name
            self.__error_message[0] = 0
        else:
            message = 'O campo Nome é obrigatório!'
            self.__error_message[0] = message

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name) -> None:
        if len(last_name) != 0:
            self.__last_name = last_name
            self.__error_message[1] = 0
        else:
            message = 'O campo Sobrenome é obrigatório'
            self.__error_message[1] = message

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username) -> None:
        if len(username) != 0:
            self.__username = username
            self.__error_message[2] = 0
        else:
            message = 'O campo username é obrigatório'
            self.__error_message[2] = message

    @property
    def password_1(self) -> str:
        return self.__password_1

    @password_1.setter
    def password_1(self, password) -> None:
        if len(password) != 0:
            if len(password) >= 5 and len(password) <= 8:
                self.__password_1 = password
                self.__error_message[3] = 0
            else:
                mensagem = 'A senha deve possuir entre 5 a 8 caracteres'
                self.__error_message[3] = mensagem
        else:
            message = 'O campo Senha é obrigatório'
            self.__error_message[3] = message

    @property
    def __password_2(self) -> str:
        return self.__password_2

    @__password_2.setter
    def __password_2(self, password) -> None:
        if len(password) != 0:
            if password == self.password_1:
                self.__password_2 = password
                self.__error_message[4] = 0
            else:
                mensagem = 'As senhas não são iguais'
                self.__error_message[4] = mensagem
        else:
            message = 'O campo Senha é obrigatório'
            self.__error_message[4] = mensagem

    @property
    def error_message(self) -> list:
        return self.__error_message

    @error_message.setter
    def error_message(self, lista) -> None:
        pass
