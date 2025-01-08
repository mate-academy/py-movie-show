from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(customer_name) for customer_name in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for person in customer_instances:
        person.CinemaBar
    cinema_hall.movie_session
    cleaner_name.clean_hall
