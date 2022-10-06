from typing import NoReturn


class Customer:
    def __init__(self, name: str, food: str) -> NoReturn:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> NoReturn:
        print(f'{self.name} is watching "{movie}".')
