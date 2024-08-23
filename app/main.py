from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_instance = [Customer(**cust) for cust in customers]
    cinemahall = CinemaHall(hall_number)
    cinemabar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for c in customer_instance:
        cinemabar.sell_product(c.food, c)
    number = CinemaHall(hall_number)

    CinemaHall.movie_session(number, movie, customer_instance, cleaner)
    pass
