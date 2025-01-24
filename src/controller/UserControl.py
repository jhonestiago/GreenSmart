from typing import List
from models.User import User

class UserControl:

    def __init__(self) -> None:
        self.__users:List[User] = []

    def add_user(self, user:User) -> None:
        message = 'Usuário adicionado com sucesso'
        self.__users.append(user)
        return message
