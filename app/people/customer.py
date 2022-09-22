class Customer:
    def __init__(self, name, food) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str):
        print(f'{self.name} is watching "{movie}".')
