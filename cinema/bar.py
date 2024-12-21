class CinemaBar:
    @staticmethod
    def sell_product(product, customer) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")

if __name__ == "__main__":
    customer = Customer("Bob", "popcorn")
    cb = CinemaBar()
    result = cb.sell_product(product=customer.food, customer=customer)
    print(result)