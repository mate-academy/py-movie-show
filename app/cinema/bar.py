from typing import AnyStr


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: AnyStr) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
