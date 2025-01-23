class Usuario:

    def __init__(self):
        self.__first_name:str = ''
        self.__last_name:str = ''
        self.__username:str = ''
        self.__password_1:str = ''
        self.__password_2:str = ''
        self.error_message:str = ''

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name) -> None:
        if len(first_name) != 0:
            self.__first_name = first_name
        else:
            message = 'O campo Nome é obrigatório!'
            self.error_message = message

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name) -> None:
        if len(last_name) != 0:
            self.__last_name = last_name
        else:
            message = 'O campo Sobrenome é obrigatório'
            self.error_message = message

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username) -> None:
        if len(username) != 0:
            self.__username = username
        else:
            message = 'O campo username é obrigatório'
            self.error_message = message

    # Continua
