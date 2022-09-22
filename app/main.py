from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = []

    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for visitor in visitors:
        cinema_bar.sell_product(visitor.food, visitor)
    CinemaHall(hall_number).movie_session(movie, visitors, cleaner)
