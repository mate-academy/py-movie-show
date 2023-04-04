from app.people import customer


class CinemaBar:
    @staticmethod
    def sell_product(visitor: customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {visitor.name}.")
