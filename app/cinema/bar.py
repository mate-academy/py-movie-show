from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer | str) -> None:
        name = customer.name if isinstance(customer, Customer) else customer
        print(f"Cinema bar sold {product} to {name}.")
