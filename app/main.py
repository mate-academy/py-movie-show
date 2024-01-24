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

    objects_list = [class_object["name"] for class_object in customers]

    for customer_object in objects_list:
        bar_class.sell_product(customer_object.food, customer_object)

    hall.movie_session(
        movie_name,
        objects_list,
        Cleaner(cleaning_staff)
    )
