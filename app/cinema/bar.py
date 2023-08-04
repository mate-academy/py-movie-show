class CinemaBar:
    @staticmethod
    def sell_product(
            customer,
            product: str) -> None:
        print(f"Cinema bar sold {product} "
              f"to {customer.name}.")
