from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = list(
        map(
            lambda customer: Customer(**customer),
            customers)
    )
    for customer in customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=Cleaner(cleaner)
    )
