from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
        bar_instance = CinemaBar()
        hall_instance = hall_number
        cleaner_instance = Cleaner(cleaner)
        customer_instances = [Customer(customer["name"], customer["food"])for customer in customers]
        for customer in customers:
                bar_instance.sell_product(customer["customer"], customer["product"])

        hall_instance.movie_session(movie, customer_instances, cleaner_instance)
