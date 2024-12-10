class CinemaBar:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def sell_product(self, customer, product, menu):
        if product in menu:
            print(f"{self.name} sold {product} to {customer['name']}.")
        else:
            print(f"Sorry, {product} is not available.")