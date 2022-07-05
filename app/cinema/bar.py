class Cinemabar:
    def __init__(self, customer, product):
        self.customer = customer
        self.product = product

    def sell_product(self):
        print(f"Cinema bar sold {self.product} to {self.customer}.")