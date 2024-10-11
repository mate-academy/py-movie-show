from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    name_and_food = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    name_cleaner = Cleaner(cleaner)

    for customer in name_and_food:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie, name_and_food, name_cleaner)
