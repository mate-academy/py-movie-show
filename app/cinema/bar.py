from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    customer_info = Customer("Bob", "popcorn")
    cb = CinemaBar()
    cb.sell_product(customer=customer_info, product=customer_info.food)
