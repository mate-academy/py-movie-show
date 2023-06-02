from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    customers_objects = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(customer, customer.food)
        customers_objects.append(customer)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_objects, cleaner)
