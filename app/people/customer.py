class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
    #    print(f"Name = {self.name}, Food = {self.food}")

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching \"{movie}\".')
