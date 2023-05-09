from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: str, hall_number: int, cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, [Customer(customer["name"], customer["food"])
                               for customer in customers], cleaning_staff)
