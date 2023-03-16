from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> any:
    list_of_customers = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    staff = Cleaner(cleaner)
    for person in list_of_customers:
        cinema_bar.sell_product(person, person.food)
    hall.movie_session(movie, list_of_customers, staff)
