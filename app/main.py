from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    class_customers = []
    for cust in customers:
        class_customers += [Customer(**cust)]

    for class_cust in class_customers:
        CinemaBar.sell_product(class_cust, class_cust.food)

    clnr = Cleaner(cleaner)

    hll = CinemaHall(hall_number)
    hll.movie_session(movie, class_customers, clnr)
