from typing import Type
from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Type[Customer]) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
