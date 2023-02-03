from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    customer_instance_list = []

    for customer in customers:
        customer["name"] = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer["name"])
        customer_instance_list.append(customer["name"])

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaning_staff)
    hall.movie_session(movie_name, customer_instance_list, cleaning_staff)
