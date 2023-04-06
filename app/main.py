from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_objs = []
    for customer in customers:
        customer_objs.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(customer_objs[-1].food, customer_objs[-1])

    cleaner = Cleaner(cleaner)
    movie_start = CinemaHall(hall_number)
    movie_start.movie_session(movie, customer_objs, cleaner)
