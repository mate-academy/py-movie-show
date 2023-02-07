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
    viewers = []
    for customer in customers:
        viewers.append(Customer(customer["name"], customer["food"]))
    bar_service = CinemaBar()
    current_hall = CinemaHall(hall_number)
    clean_serve = Cleaner(cleaner)
    for one in viewers:
        bar_service.sell_product(one, one.food)
    current_hall.movie_session(movie, viewers, clean_serve)
