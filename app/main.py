from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []

    for cs in customers:
        customers_list.append(Customer(cs["name"], cs["food"]))

    for cs in customers_list:
        CinemaBar.sell_product(cs, cs.food)

    cinema_wathing = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cinema_wathing.movie_session(movie, customers_list, clean)
