from app.people.customers import Customer


class CinemaBar:
    @staticmethod
    def sell_prduct(customer, product):
        print(f"Cinema bar sold {product} to {customer.name}.")
