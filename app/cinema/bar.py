class CinemaBar():
    @staticmethod
    def sell_product(customer: str, product: str) -> None:
        # customer is instance class Customer
        print(f"Cinema bar sold {product} to {customer.name}.")
