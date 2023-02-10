from app.people.customer import *


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        result = f"Cinema bar sold {product} to {customer.name}."
        print(result)

cb = CinemaBar()

#customer = Customer("Bob", "popcorn", ["Bob", "Gop", "Tor"])
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)
