from app.people.customer import Customer


class CinemaBar:
    def __init__(self, product: str = "Nothing") -> None:
        self.product = product

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        if customer.food:
            print(f"Cinema bar sold {customer.food} to {customer.name}.")
        else:
            print(f"Cinema bar sold {product} to {customer.name}.")
