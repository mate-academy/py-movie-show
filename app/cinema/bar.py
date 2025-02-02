from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, food: str) -> None:
        print(f"Cinema bar sold {food} to {customer.name}.")
