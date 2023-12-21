from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cleaning = Cleaner(cleaner)
    # ----------------------------------how many customers came to the movie
    for person in customers:
        if isinstance(person, Customer):
            CinemaBar.sell_product(person, person.food)
        else:
            customer = Customer(person["name"], person["food"])
            CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(movie, customers, cleaning)
