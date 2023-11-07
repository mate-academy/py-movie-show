from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    pass

    @staticmethod
    def sell_product(customer: Customer, product: Customer) -> None:
        print(f"Cinema bar sold {customer.food} to {customer.name}.")
