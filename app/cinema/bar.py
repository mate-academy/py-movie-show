from typing import Callable


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Callable) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
