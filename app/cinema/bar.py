from ..people import customer as cstmr


class CinemaBar:
    @staticmethod
    def sell_product(customer: cstmr.Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
