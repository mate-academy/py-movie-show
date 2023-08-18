from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    """This class describes work of cinema bar"""

    # def __init__(self, product, customer) -> None:
    #     self.product = product
    #     self.customer = customer

    @staticmethod
    def sell_product(customer: Customer, product: str):
        print(f"Cinema bar sold {product} to {customer.name}.")
