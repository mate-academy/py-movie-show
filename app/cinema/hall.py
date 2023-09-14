class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list[object],
                      cleaning_staff: object) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')
        for cust in customers:
            cust.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
