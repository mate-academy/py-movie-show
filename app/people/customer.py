class Customer:
    def __init__(self, name: str, food: str):
        self.customer = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.customer} is watching "{movie}".')
