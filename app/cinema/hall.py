from app.people.customer import Customer


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
