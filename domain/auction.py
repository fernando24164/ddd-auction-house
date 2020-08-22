from typing import List, Dict
from dataclasses import dataclass, field, InitVar
from uuid import uuid4
from datetime import datetime, timedelta

from domain.user import User
from domain.item import Item
from domain.money import Money
from domain.bid import Bid
from domain.exceptions import NotFoundException


@dataclass
class Auction:
    creator: User
    auction_id: str = field(default_factory=uuid4)
    due_date: datetime = field(
        default_factory=lambda: datetime.now() + timedelta(days=7)
    )
    items: List[Item] = field(default_factory=list)
    bids: List[Money] = field(default_factory=list)
    winner: Bid = None
    external_check_needed = InitVar[bool]

    def __post_init__(self):
        try:
            for item in self.items:
                self.creator.remove_item(item.item_id)
        except NotFoundException:
            self.external_check_needed = True

    def update_auction(self, params: Dict):
        for k, v in params.items():
            setattr(self, k, v)

    def make_bid(self, bid: Bid) -> bool:
        def _bid_checker(bid: Bid) -> bool:
            return (
                self.winner is None or bid > self.winner
            ) and bid.player != self.creator

        if _bid_checker(bid):
            self.bids.append(bid)
            self.winner = bid
            return True
        return False
