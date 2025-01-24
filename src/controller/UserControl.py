from typing import List
from models.User import User

class UserControl:

    def __init__(self) -> None:
        self.__users:List[User] = []

    def add_user(self, user:User) -> str:
        self.__users.append(user)
        return 'Usuário adicionado com sucesso'

    def remove_user(self, index:int) -> str:
        del self.__users[index]
        return 'Usuário removido com sucesso'
