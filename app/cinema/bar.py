from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(cust: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {cust.name}")
