from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    list_visitors = []
    cleaner_person = Cleaner(cleaner)
    hall = CinemaHall(number)

    list_visitors = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    for customer in list_visitors:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, list_visitors, cleaner_person)
