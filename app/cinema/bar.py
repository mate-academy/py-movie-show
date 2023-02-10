from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        customer_check = (customer.name if isinstance(customer, Customer)
                          else customer)
        print(f"Cinema bar sold {product} to {customer_check}.")
