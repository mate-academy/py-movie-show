from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_stuff: Cleaner
    ) -> None:
        num = self.number
        print(f'\"{movie_name}\" started in hall number {num}.')
        for el in customers:
            el.watch_movie(movie=movie_name)
        print(f'\"{movie_name}\" ended.')
        # clean_person = Cleaner(cleaning_stuff)
        cleaning_stuff.clean_hall(hall_number=num)


# if __name__ == "__main__":
#     bob = Customer(name="Bob", food="popcorn")
#     fil = Customer(name="Fil", food="popcorn")
#     elza = Cleaner(name="Elza")
#     customers = [bob, fil]
#     num = CinemaHall(number=5)
#     num.movie_session(
#         movie_name="Madagascar",
#         customers=customers,
#         cleaning_stuff=elza)
