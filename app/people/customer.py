class Customer:
    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food

    def __str__(self):
        return self.name

    def watch_movie(self, movie: str):
        print(f'{self.name} is watching "{movie}".')

