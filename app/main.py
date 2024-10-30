from app.cinema import CinemaHall
from app.people import Customer
from app.people import Cleaner
from app.cinema import CinemaBar
from typing import Any


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> Any:
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_objects, cleaning_staff)
