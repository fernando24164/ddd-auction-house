from abc import ABC

from domain.auction import Auction


class AuctionRepository(ABC):
    def add(self, auction: Auction):
        raise NotImplementedError

    def update(self, id_auction: str, auction: Auction):
        raise NotImplementedError

    def delete(self, id_auction: str):
        raise NotImplementedError

    def list_all(self):
        raise NotImplementedError

    def get(self, id_auction: str):
        raise NotImplementedError
