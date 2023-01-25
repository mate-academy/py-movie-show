from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    cstm = []
    for customer in customers:
        cstm.append(Customer(customer["name"], customer["food"]))
    bar1 = CinemaBar()
    c_hall = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    for one in cstm:
        bar1.sell_product(one, one.food)
    c_hall.movie_session(movie, cstm, cleaner1)
