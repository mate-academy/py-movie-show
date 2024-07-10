from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = [Customer(customer["name"], customer["food"]) for customer in customers]

    hall = CinemaHall(hall_number)

    bar = CinemaBar()

    cleaner = Cleaner(cleaner)

    for customer in customer_instances:
        bar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_instances, cleaner)
