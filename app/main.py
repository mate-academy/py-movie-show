from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(name = c["name"], food =c["food"]) for c in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(product = customer.food, customer = customer)

    cinema_hall = CinemaHall(hall_number = hall_number)

    cleaner_instance = Cleaner(name = cleaner)

    cinema_hall.movie_session(movie_name = movie, customers = customer_objects, cleaning_staff = cleaner_instance)
