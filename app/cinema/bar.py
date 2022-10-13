# from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer, product):
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == '__main__':
    cb = CinemaBar()
    customer = Customer(name="Bob", food="popcorn")
    cb.sell_product(customer=customer, product=customer.food)
    # Cinema bar sold popcorn to Bob.
