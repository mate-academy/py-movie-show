from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_instances, cleaner)
