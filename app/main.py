from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: Cleaner(Customer),
        movie: str) -> None:
    for customer in customers:
        CinemaBar.sell_product(customer["food"], customer["name"])
    CinemaHall(hall_number).movie_session(movie, customers, cleaner)
