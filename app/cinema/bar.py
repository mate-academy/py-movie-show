from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        TODO
        add "__future__" and change to Customer class
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
