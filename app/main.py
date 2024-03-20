from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers = [Customer(**customer) for customer in customers]
    list(map(lambda x: CinemaBar().sell_product(x, x.food), customers))
    CinemaHall(hall_number).movie_session(movie, customers, Cleaner(cleaner))
