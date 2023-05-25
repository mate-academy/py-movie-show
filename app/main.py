from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_objs = []
    clean = Cleaner(cleaner)

    for person in customers:
        customers_objs.append(Customer(person["name"], person["food"]))

    for person in customers_objs:
        CinemaBar.sell_product(person.food, person)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_objs, clean)
