from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer}.")

# if __name__ == "__main__":
#     from app.people.customer import Customer
#
#     cb = CinemaBar()
#     customer = Customer("Bob", "popcorn")
#     print(cb.sell_product(customer=customer.name, product=customer.food))
#     # Cinema bar sold popcorn to Bob.
