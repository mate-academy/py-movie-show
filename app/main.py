from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaners = Cleaner(cleaner_name)
    customer_list = [Customer(c.get("name"), c.get("food")) for c in customers]
    for customer in customer_list:
        cb.sell_product(customer, customer.food)
    hall.movie_session(
        movie_name, customer_list, cleaners)
