from __future__ import annotations


class Customer:

    def __init__(self, name: Customer, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}"')


bob = Customer(name="Bob", food="popcorn")
bob.watch_movie(movie="Madagascar")
