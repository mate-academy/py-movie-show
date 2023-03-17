from __future__ import annotations


class Customer:
    def __init__(self, name: str, food: str) -> Customer:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> str:
        print(f'{self.name} is watching "{movie}".')


if __name__ == "__main__":
    bob = Customer(name="Bob", food="popcorn")
    bob.watch_movie(movie="Madagascar")
    # Bob is watching "Madagascar".
