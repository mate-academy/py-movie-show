from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaning_staff)
