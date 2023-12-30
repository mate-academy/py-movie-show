class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
        Customer.customers.append(self)

    customers = []

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
