from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall_ = CinemaHall(hall_number)
    bar_ = CinemaBar()
    cleaner_ = Cleaner(cleaner)
    customers_list_ = []
    for person in customers:
        customers_list_.append(Customer(person["name"], person["food"]))
    for person in customers_list_:
        bar_.sell_product(person, person.food)
    hall_.movie_session(movie, customers_list_, cleaner_)
