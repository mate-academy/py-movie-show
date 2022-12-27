from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    lst = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        lst.append(customer)
    hall_num = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for customer in lst:
        cinema_bar.sell_product(customer.food, customer)
    hall_num.movie_session(movie, lst, cleaner)
