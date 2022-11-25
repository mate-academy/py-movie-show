from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaner: Cleaner
    ) -> None:

<<<<<<< HEAD
        print(f'"{movie_name}" started in hall number {self.number}.')
        for person in customers:
            person.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
=======
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for person in customers:
            # one_customer = Customer(**person)
            person.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
>>>>>>> 8a0cf225de1c1d9d1123ba0233a2f852bd01be29
        cleaner.clean_hall(self.number)
