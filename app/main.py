from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> str:
    customers_instances = []
    for customer in customers:
        customers_instances.append(
            Customer(customer["name"], customer["food"])
        )
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)
    for object_ in customers_instances:
        cinema_bar.sell_product(object_.food, object_)
    cinema_hall.movie_session(movie, customers_instances, cleaner_staff)
