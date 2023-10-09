class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movies: str) -> str:
        print(f'{self.name} is watching "{movies}".')
