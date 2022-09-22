from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


#
# CinemaHall(number=5).movie_session(
#     movie_name="Madagascar",
#     customers=[Customer("Anna", "popcorn"), Customer("Liuda", "cola")],
#     cleaning_staff=Cleaner("Mykola")
# )
