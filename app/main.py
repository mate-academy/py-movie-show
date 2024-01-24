from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    bar_class = CinemaBar()
    hall = CinemaHall(hall_number)
    for customer in customers:
        customer["name"] = Customer(customer["name"], customer["food"])
        bar_class.sell_product(customer["name"] .food, customer["name"])
    hall.movie_session(
        movie_name,
        [class_object["name"] for class_object in customers],
        Cleaner(cleaning_staff)
    )
