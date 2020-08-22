from abc import ABC

from domain.user import User

class UserRepository(ABC):
    def add(self, user: User):
        raise NotImplementedError

    def update(self, id_user: str, user: User):
        raise NotImplementedError

    def delete(self, id_user: str):
        raise NotImplementedError

    def list_all(self):
        raise NotImplementedError

    def get(self, id_user: str):
        raise NotImplementedError

