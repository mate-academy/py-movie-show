from __future__ import annotations
from app.people.cinema_staff import Cleaner


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching \"{movie}\".')

    @classmethod
    def customer_extractor(cls, customer_list: list) -> list[Customer]:
        return [
            cls(
                name=customer["name"],
                food=customer["food"]
            )
            for customer in customer_list
        ]
