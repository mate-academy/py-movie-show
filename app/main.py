from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = Customer(customers)
    number = CinemaHall(hall_number)
    movie_name = CinemaBar(movie)
    cleaner = Cleaner(cleaner)
