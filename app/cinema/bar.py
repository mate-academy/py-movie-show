from app.people import customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
