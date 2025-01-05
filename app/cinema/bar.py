from app.people.customer import Customer

class CinemaBar:
    @staticmethod
    def sell_product(product: str, customers: Customer) -> None:
        print(f"Cinema bar sold {product} to {customers} ")
