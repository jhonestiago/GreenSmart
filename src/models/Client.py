import numpy as np

class Client:

    def __init__(self) -> None:
        self.__name = None
        self.__cpf_cnpj = None
        self.__address = None
        self.__email = None
        self.__phone_number = None
        self.__error_message = np.zeros(3,dtype=object)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if len(name) == 0:
            message = 'O campo Nome Completo é obrigatório'
            self.__error_message[0] = message
        else:
            self.__name = name

    @property
    def cpf_cnpj(self) -> str:
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj) -> None:
        if len(cpf_cnpj) == 0:
            message = 'O campo CPF/CNPJ é obrigatório'
            self.__error_message[1] = message
        else:
            self.__cpf_cnpj = cpf_cnpj

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address:str) -> None:
        self.__address = address

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        if len(email) == 0:
            message = 'O campo E-mail é obrigatório'
            self.__error_message[2] = message
        else:
            self.__email = email

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number) -> None:
        self.__phone_number = phone_number

    @property
    def error_message(self) -> list:
        return self.__error_message

    @error_message.setter
    def error_message(self, list:list) -> None:
        pass
