from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    for customer_in_loop in customers:
        CinemaBar.sell_product(Customer(customer_in_loop))

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=Cleaner(cleaner)
    )
