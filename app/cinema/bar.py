from typing import Any


class CinemaBar:

    @staticmethod
    def sell_product(customer: Any, customer_food: str) -> None:
        print(f"Cinema bar sold {customer_food} to {customer.name}.")
