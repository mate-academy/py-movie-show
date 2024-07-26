from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    customers_objects = [Customer(c["name"], c["food"]) for c in customers]
    for customer in customers_objects:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_objects, Cleaner(cleaner))
