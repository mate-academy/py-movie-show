from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = [Customer(customer.get("name"), customer.get("food")) for customer in customers]

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    cleaner_1 = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    CinemaHall.movie_session(hall, movie, customers_list, cleaner_1)
