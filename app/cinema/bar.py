from app.people.customer import Customer


class CinemaBar:
    def sell_product(self, customer: Customer, product: str) -> None:
        print("Cinema bar sold " + product + " to " + customer.name + ".")
