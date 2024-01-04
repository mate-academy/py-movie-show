from typing import Callable, List


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List[Callable],
            clearing_staff: Callable
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        
        for customer in customers:
            customer.watch_movie(movie_name)
        
        print(f'"{movie_name}" ended.')
        clearing_staff.clean_hall(self.number)
