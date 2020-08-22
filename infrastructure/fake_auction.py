from typing import Iterator, Dict, List

from .auction_interface import AuctionRepository
from .exceptions import NotFoundException
from domain.auction import Auction


class FakeAuctionRepository(AuctionRepository):
    def __init__(self):
        super().__init__()
        self.auctions: List[User]  = []

    def add(self, auction: Auction):
        self.auctions.append(auction)

    def update(self, id_auction: str, params: Dict) -> bool:
        for index, ele in enumerate(self.auctions):
            if ele.auction_id == id_auction:
                self.auctions[index].update_auction(params)
                return True
        return False

    def delete(self, id_auction: str) -> bool:
        """Delete one auction from DB

        :param id_auction: Id to identy auction
        :type id_auction: str
        :raises NotFoundException: Exception in case the id is not found
        :return: True if deleted
        :rtype: bool
        """
        for index, ele in enumerate(self.auctions):
            if ele.auction_id == id_auction:
                del self.auctions[index]
                return True
        raise NotFoundException

    def list_all(self) -> Iterator[Auction]:
        for element in self.auctions:
            yield element

    def get(self, id_auction: str) -> Auction:
        for index, ele in enumerate(self.auctions):
            if ele.auction_id == id_auction:
                return self.auctions[index]
        raise NotFoundException
