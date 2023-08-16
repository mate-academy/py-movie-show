class CinemaBar:
    @staticmethod
    def sell_product(customer: callable, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
