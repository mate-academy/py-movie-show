from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    new_customers = [Customer(customer["name"],
                              customer["food"])
                     for customer in customers]
    hall_number = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in new_customers:
        cinema_bar.sell_product(customer.food, customer)
    hall_number.movie_session(movie, new_customers, cleaner)
