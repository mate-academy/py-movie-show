from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    for customer in customers:
        CinemaBar.sell_product(customer["name"], customer["food"])
    hall.movie_session(movie, customer_list, cleaner_name)
