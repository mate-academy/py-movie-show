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
    customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customers:
        cinema_bar.sell_product(customer.name, customer.food)
    cinema_hall.movie_session(
        movie,
        customers,
        cleaner
    )
