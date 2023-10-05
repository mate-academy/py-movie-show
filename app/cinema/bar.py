class CinemaBar:

    @staticmethod
    def sell_product(client: "Customer", product: str) -> None:
        print(f"Cinema bar sold {product} to {client}")
