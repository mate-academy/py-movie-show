from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_new = []
    for human in customers:
        customers_new.append(Customer(human["name"], human["food"]))
    for human in customers_new:
        CinemaBar.sell_product(human, human.food)
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie,
                             customers_new,
                             Cleaner(cleaner))
