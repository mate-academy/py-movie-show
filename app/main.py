from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        customer_any = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_any)
    cleaner_now = Cleaner(cleaner)
    cinema_now = CinemaHall(hall_number)
    cinema_now.movie_session(movie, customers, cleaner_now)
