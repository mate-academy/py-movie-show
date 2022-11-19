from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_cust_class = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_cust_class.append(new_customer)
    hall_num = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for bar_cust in list_cust_class:
        CinemaBar.sell_product(bar_cust.food, bar_cust)
    hall_num.movie_session(movie, list_cust_class, clean)
