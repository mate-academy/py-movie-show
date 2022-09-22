from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cb_class = CinemaBar()
    ch_class = CinemaHall(hall_number)
    cl_class = Cleaner(cleaner)
    list_of_cast = []
    for cast in customers:
        list_of_cast.append(Customer(cast.get("name"), cast.get("food")))
    for one_cast in list_of_cast:
        cb_class.sell_product(one_cast.food, one_cast)
    ch_class.movie_session(movie, list_of_cast, cl_class)
