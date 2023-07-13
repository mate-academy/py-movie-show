from typing import Any


class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> Any:
        print(f'{self.name} is watching "{movie}".')
