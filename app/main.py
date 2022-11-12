from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    c_b = CinemaBar()
    customers_list = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        c_b.sell_product(product=cust.food, customer=cust)
        customers_list.append(cust)
    c_h = CinemaHall(hall_number)
    cl_st = Cleaner(cleaner)
    c_h.movie_session(
        movie_name=movie, customers=customers_list, cleaning_staff=cl_st
    )
