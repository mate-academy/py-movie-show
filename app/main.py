from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cleaning_person = Cleaner(cleaner)
    cinema = CinemaHall(hall_number)
    list_customers = [Customer(i["name"], i["food"]) for i in customers]
    for customer in list_customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema.movie_session(movie, list_customers, cleaning_person)
