from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"Cinema bar sold {product} to {customer.name}.")


cb = CinemaBar()
customer_ = Customer("Bob", "popcorn")
cb.sell_product(customer=customer_, product=customer_.food)
