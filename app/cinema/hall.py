class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list,
        cleaning_staff: str
    ) -> str:
        print(f'"{movie_name}" started in hall number {self.number}.')
        list(map(lambda customer: customer.watch_movie(movie_name), customers))
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
