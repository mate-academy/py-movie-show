from app.cinema.bar import Cinemabar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for c in customers:
        Customer(c["name"], c["food"])

    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    for c in customers:
        CinemaBar.sell_product(customer=c[0], product=c[1])
    Cinemahall.movie_session(hall_number, movie, customers, cleaner)
