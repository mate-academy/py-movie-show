from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_list = []
    for customer in customers:
        custom = Customer(name=customer["name"], food=customer["food"])
        customer_list.append(custom)
        CinemaBar.sell_product(custom.food, custom)
    cleaner_name = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customer_list, cleaner_name)
