from app.cinema.customer import Customer

class CineBar:

    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"Cinema bar sold {product} to {customer}.")

