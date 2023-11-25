from app.peaple.customer import Customer
from app.peaple.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number
    # number of the hall in cinema

    def movie_session(self, movie: str, customers: list,
                      cleaning_staff: str) -> str:
        print(f"{movie} started in hall number {self.number}")
        for i in customers:
            cs = Customer(i["name"], i["food"])
            cs.watch_movie(movie)
        print(f"{movie} ended")
        cl = Cleaner(cleaning_staff)
        cl.clean_hall(self.number)
