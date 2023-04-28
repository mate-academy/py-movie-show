from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

Customer("Anton", "apple")
Cleaner("Anton")


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    for customer in customers:
        CinemaBar.sell_product(customer["food"], customer["name"])
    CinemaHall(hall_number).movie_session(movie, customers, cleaner)
