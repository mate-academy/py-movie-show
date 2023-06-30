from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer = []
    for person in customers:
        customer.append(Customer(person["name"], person["food"]))
    for human in customer:
        CinemaBar.sell_product(human, human.food)
    cleaner_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer, cleaner_staff)
