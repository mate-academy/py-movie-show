from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    people = []
    for customer in customers:
        customer = (Customer(customer["name"], customer["food"]))
        people.append(customer)
        CinemaBar()
        CinemaBar.sell_product(customer, customer.food)
    cinema = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cinema.movie_session(movie, people, clean)
