from app.bar import CinemaBar
from app.hall import CinemaHall
from app.customer import Customer
from app.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)
    customer_objects = [Customer(customer["name"], customer["food"]) for customer in customers]

    cinema_bar = CinemaBar()
    for customer in customer_objects:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_object)
