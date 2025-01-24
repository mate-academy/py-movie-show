from cinema.bar import CineBar
from app.cinema.hall import CinemaHall
from app.cinema.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for person in customers:
        CineBar.sell_product(person["name"],person["food"])
    CinemaHall(hall_number).movie_session(movie, customers, Cleaner(name = cleaner))







