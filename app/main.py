from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        CinemaBar.sell_product(Customer(customer["name"],
                                        customer["food"]),
                               Customer(customer["name"],
                                        customer["food"]).food,)
    return CinemaHall(hall_number).movie_session(movie, customers, cleaner)
