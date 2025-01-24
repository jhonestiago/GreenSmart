from typing import List
from models.User import User

class UserControl:

    def __init__(self) -> None:
        self.__users:List[User] = []

    def add_client(self, user:User) -> None:
        self.__users.append(user)
