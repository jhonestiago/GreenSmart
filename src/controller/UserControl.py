from typing import List
from src.models.User import User

class UserControl:

    def __init__(self) -> None:
        self.__users:List[User] = []

    def add_user(self, user:User) -> str:
        '''
        Adiciona um usuário à lista de usuários.
        '''
        self.__users.append(user)
        return 'Usuário adicionado com sucesso'

    def find_user(self, username:str, password:str) -> bool:
        '''
        Verifica se um usuário com as credenciais 
        fornecidas existe na lista de usuários.
        '''
        access_key = False
        for user in self.__users:
            if (user.username == username) and (user.password_1 == password):
                access_key = True
                break
        return access_key

    def get_user(self, index:int) -> User:
        '''
        Retorna um usuário específico pelo índice.
        '''
        return self.__users[index]

    def update_user(self, index:int, user:User) -> str:
        '''
        Atualiza os dados de um usuário na lista pelo índice.
        '''
        self.__users[index] = user
        return 'Usuário atualizado com sucesso'

    def remove_user(self, index:int) -> str:
        '''
        Remove um usuário da lista de usuários pelo índice.
        '''
        del self.__users[index]
        return 'Usuário removido com sucesso'

    @property
    def users(self) -> List[User]:
        '''
        Retorna a lista de usuários.
        '''
        return self.__users

    @users.setter
    def users(self, users_list: List[User]) -> None:
        pass
