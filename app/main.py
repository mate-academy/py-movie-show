from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_ls = []
    for i in customers:
        customer = Customer(i["name"], i["food"])
        customers_ls.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    CinemaHall.movie_session(hall, movie, customers_ls, Cleaner(cleaner))
