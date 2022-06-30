from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, hall_number, cleaner, movie):
    ls_of_cls_obj = [Customer(obj["name"], obj["food"]) for obj in customers]
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    for customer in ls_of_cls_obj:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall.movie_session(hall_number, movie, ls_of_cls_obj, cleaner)
