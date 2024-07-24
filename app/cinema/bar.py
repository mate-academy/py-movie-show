from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> str:
        print(f"Selling {product} to {customer.name}.")
