import app.people.customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: app.people.customer.Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
