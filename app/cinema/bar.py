from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        print(f'Cinema bar sold {product} to {customer.name}.')


if __name__ == "__main__":
    cb = CinemaBar()
    first_customer = Customer("Bob", "popcorn")
    cb.sell_product(customer=first_customer, product=first_customer.food)
