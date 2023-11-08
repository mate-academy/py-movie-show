from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaBar:

    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"Cinema bar sold {product} to {customer.name}.")
