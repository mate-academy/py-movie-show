from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for visitor in list_of_customers:
        CinemaBar.sell_product(visitor, visitor.food)

    hall.movie_session(movie, list_of_customers, cleaner_name)
