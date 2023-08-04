class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        print(f"Movie session in Hall {self.number} is starting with movie '{movie_name}'.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print("Movie session has ended.")

        cleaning_staff.clean_hall()


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name

    def watch_movie(self, movie_name: str) -> None:
        print(f"{self.name} is watching {movie_name}.")


class Cleaner:
    @staticmethod
    def clean_hall() -> None:
        print("Cleaner is cleaning the hall.")
