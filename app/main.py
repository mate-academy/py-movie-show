from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    people = []
    staff = Cleaner(cleaner)

    for customer in customers:
        unit = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(unit, customer["food"])
        people.append(unit)

    hall.movie_session(
        movie,
        people,
        staff,
    )
