from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    cinema_bar = CinemaBar()
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)

    for customer_instance in customer_list:
        cinema_bar.sell_product(product=customer_instance.food,
                                customer=customer_instance)
    hall.movie_session(movie_name=movie,
                       customers=customer_list,
                       cleaning_staff=staff)
