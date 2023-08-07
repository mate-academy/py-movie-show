from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print("Cinema bar sold {} to {}.".format(
            product,
            customer.name)
        )
