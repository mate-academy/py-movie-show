from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_instances = [Customer(name=c["name"],
                                   food=c["food"]) for c in customers]
    cleaner_instance = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
