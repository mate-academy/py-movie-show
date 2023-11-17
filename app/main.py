from typing import Any

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> Any:
    cinema_bar = CinemaBar()
    customers_list = []
    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        cinema_bar.sell_product(customer=customer, product=customer.food)
        customers_list.append(customer_info)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
