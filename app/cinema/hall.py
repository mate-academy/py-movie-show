class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie_name: str) -> None:
        print(
            f"{self.name} "
            f"is watching {movie_name} "
            f"while eating {self.food}."
        )


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"{self.name} is cleaning hall {hall_number}.")


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str,
            customers: Customer,
            cleaning_staff: str
    ) -> None:
        print(f"Starting movie '{movie_name}' in hall {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie '{movie_name}' has ended in hall {self.number}.")
        cleaning_staff.clean_hall(self.number)
