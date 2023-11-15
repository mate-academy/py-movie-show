class Customer:
    people = []

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
        self.people.append(self)

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
