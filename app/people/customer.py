from __future__ import annotations


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        # Flake8 asks to change the outer quotes to single
        # ones to avoid escaping (\") inside the f-string.
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

# ERROR collecting tests/test_cleaner.py
# ERROR collecting tests/test_hall.py
# ImportError: cannot import name 'Cleaner' from 'app.people.customer'
# ____________
# For some reason, in the tests, the program wants to
# import it exactly like this, so I copied this code here.


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
