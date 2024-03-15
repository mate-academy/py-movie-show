class CinemaHall:
    def __init__(self, number: int) -> int:
        self.number = number

    def movie_session(
            self, movie_name: str, customers: str, cleaning_staff: str
    ) -> None:
        print(
            f"""Movie session for '{movie_name}'
              has started in Hall {self.number}.""")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"""Movie session for '{movie_name}'
               has ended in Hall {self.number}.""")

        cleaning_staff.clean_hall()


class Customer:
    def watch_movie(self) -> None:
        print("Customer is watching the movie.")


class Cleaner:
    def clean_hall(self) -> None:
        print("Cleaning staff is cleaning the hall.")
