from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number) -> None:
        self.number = number

    def movie_session(
            self, movie_name, customers: list, current_cleaner: Cleaner
    ) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for person in customers:
            person.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        current_cleaner.clean_hall(self.number)
