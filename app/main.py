from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> object:
    customers_list = []
    our_cleaner = Cleaner(cleaner)
    for i in customers:
        customer = Customer(i["name"], i["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer, i["food"])
    CinemaHall(hall_number).movie_session(movie, customers_list, our_cleaner)
