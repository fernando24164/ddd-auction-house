from typing import Dict, Iterator, List

from .exceptions import NotFoundException
from domain.user import User
from infrastructure.user_interface import UserRepository


class FakeUserRepository(UserRepository):
    def __init__(self):
        super().__init__()
        self.users: List[User] = []

    def add(self, user: User) -> bool:
        for ele in self.users:
            if ele.user_id == user.user_id:
                return False
        self.users.append(user)
        return True

    def delete(self, id_user) -> bool:
        """Delete one user from DB

        :param id_user: Id to identy user
        :type id_user: str
        :raises NotFoundException: Exception in case the id is not found
        :return: True if deleted
        :rtype: bool
        """
        for index, ele in enumerate(self.users):
            if ele.user_id == id_user:
                del self.users[index]
                return True
        raise NotFoundException

    def list_all(self) -> Iterator[User]:
        for element in self.users:
            yield element

    def get(self, id_user) -> User:
        for index, ele in enumerate(self.users):
            if ele.user_id == id_user:
                return self.users[index]
        raise NotFoundException
