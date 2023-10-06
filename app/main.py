from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaning_staff: str,
    movie: str
) -> None:

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaning = Cleaner(cleaning_staff)

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer)

        cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
    cinema_cleaning.clean_hall(hall_number)
