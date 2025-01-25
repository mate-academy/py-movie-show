class Customer:
    def __init__(self, name):
        self.name = name
class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f'Cinema bar sold {product} to {customer.name}.')