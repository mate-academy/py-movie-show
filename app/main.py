from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    Customer("name", "food")
    Cleaner("name")
    for customer in customers:
        CinemaBar.sell_product(customer["food"], customer["name"])
    CinemaHall(hall_number).movie_session(customers, cleaner, movie)
