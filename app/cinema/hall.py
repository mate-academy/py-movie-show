from typing import AnyStr


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_stuff: AnyStr
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for name in customers:
            name.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_stuff.clean_hall(self.number)
