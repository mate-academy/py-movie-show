from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    instance_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    instance_cinema_bar = CinemaBar()
    instance_cinema_hall = CinemaHall(
        hall_number
    )
    instance_cleaner = Cleaner(cleaner)
    for instance in instance_customers:
        instance_cinema_bar.sell_product(instance.food, instance)
    instance_cinema_hall.movie_session(
        movie, instance_customers, instance_cleaner
    )
