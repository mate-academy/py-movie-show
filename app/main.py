from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:

    instances = [
        Customer(name=ins["name"], food=ins["food"]) for ins in customers
    ]

    cinema_bar = CinemaBar()
    for customer in instances:
        cinema_bar.sell_product(customer, customer.food)

    cleaner_instance = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=instances,
        cleaning_staff=cleaner_instance
    )
