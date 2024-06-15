from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str,) -> None:
    customer_object = [Customer(customer["name"], customer["food"]) for customer in customers]
    cleaner_object = Cleaner(cleaning_staff)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    for customer in customer_object:
        cinema_bar.sell_product(customer.food, customer)
    hall.movie_session(movie_name, customer_object, cleaner_object)
