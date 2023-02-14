from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    customer_list = []
    for customer in customers:
        customer = Customer(customer.get("name"), customer.get("food"))
        customer_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_list, cleaner)
