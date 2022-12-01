from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_customers = [Customer(guest["name"], guest["food"])
                      for guest in customers
                      ]
    cleaner = Cleaner(cleaner)
    for guest in list_customers:
        CinemaBar.sell_product(guest, guest.food)
    CinemaHall(hall_number).movie_session(movie, list_customers, cleaner)
