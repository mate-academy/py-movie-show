from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    customers_instances = []
    hall_cleaner = Cleaner(cleaner_name)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customers:
        customers_instances.append(
            Customer(customer.get("name"), customer.get("food"))
        )

    for customer in customers_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_stuff=hall_cleaner
    )
