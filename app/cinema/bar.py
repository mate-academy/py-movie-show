from app.people.customer import Customer

class CinemaBar:
    @staticmethod
    def sell_product(customer, product):
        print(f"Cinema bar sold {product} to {customer}.")


cb = CinemaBar()
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)
# Cinema bar sold popcorn to Bob.