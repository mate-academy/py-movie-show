from __future__ import annotations


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"\"{movie_name}\" ended.")

        cleaning_staff.clean_hall(self.number)


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name

    def watch_movie(self, movie_name: str) -> None:
        print(f"{self.name} is watching {movie_name}.")


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
