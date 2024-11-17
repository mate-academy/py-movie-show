from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str | Customer) -> None:
        print(f"Cinema bar sold {customer.food} to {customer.name}.")