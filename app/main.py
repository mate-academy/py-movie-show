from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    customers_list = []
    cleaner = Cleaner(cleaner)
    for customer in customers:
        cust = Customer(customer['name'], customer['food'])
        customers_list.append(cust)
        CinemaBar.sell_product(customer['food'], cust)

    hall.movie_session(movie, customers_list, cleaner)