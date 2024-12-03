class CinemaBar:
    def __init__(self):
        pass

    @staticmethod
    def sell_product(product: str, customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
