from app.people.customer import CustomerAlias


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: CustomerAlias) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
