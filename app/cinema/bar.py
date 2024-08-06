from app.people.customer import Customer


class CinemaBar:

    @classmethod
    def sell_product(cls, customer: Customer, product: str):
        print(f"Cinema bar sold {product} to {customer.name}.")
