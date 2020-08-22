from domain.auction import Auction
from domain.user import User

from infrastructure.auction_interface import AuctionRepository
from infrastructure.user_interface import UserRepository


def handler_create_auction(repository: AuctionRepository, auction: Auction):
    repository.add(auction)


def handler_get_auction(repository: AuctionRepository, auction: Auction):
    repository.get(auction.auction_id)


def handler_list_auctions(repository: AuctionRepository):
    repository.list_all()


def handler_delete_auction(repository: AuctionRepository, auction: Auction):
    repository.delete(auction.auction_id)


def handler_create_user(repository: UserRepository, user: User):
    repository.add(user)


def handler_get_user(repository: UserRepository, user: User):
    repository.get(user.user_id)


def handler_list_users(repository: UserRepository):
    repository.list_all()


def handler_delete_user(repository: UserRepository, user: User):
    repository.delete(user.user_id)
