from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(name=customer.get("name"), food=customer.get("food")))
    staff = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer.name)
    CinemaHall.movie_session(CinemaHall(hall_number), movie_name=movie, customers=customers_list, cleaning_staff=staff)



