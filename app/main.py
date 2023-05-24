from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cust = []
    clean = Cleaner(cleaner)

    for person in customers:
        cust.append(Customer(person["name"], person["food"]))

    for person in cust:
        CinemaBar.sell_product(person.food, person)

    hl = CinemaHall(hall_number)
    hl.movie_session(movie, cust, clean)
