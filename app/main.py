# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers = [Customer(p["name"], p["food"]) for p in customers]
    ch = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for p in customers:
        CinemaBar.sell_product(p, p.food)
    ch.movie_session(movie, customers, cleaner_staff)
