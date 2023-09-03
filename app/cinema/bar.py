from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, costumer: "Customer") -> None:
        print(f"Cinema bar sold {product} to {costumer.name}")
