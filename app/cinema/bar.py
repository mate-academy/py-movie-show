from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str):
        return f"Sold {product} to {customer.name}!"
