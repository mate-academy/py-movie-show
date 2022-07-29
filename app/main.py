from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
):

    cinema_visitors = [
        Customer(
            customer["name"],
            customer["food"])
        for customer in customers
    ]

    for visitor in cinema_visitors:
        CinemaBar.sell_product(visitor.food, visitor)

    CinemaHall(hall_number).movie_session(
        movie_name,
        cinema_visitors,
        Cleaner(cleaning_staff)
    )
