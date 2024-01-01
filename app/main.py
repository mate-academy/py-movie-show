from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int = CinemaHall,
                 cleaner: str = Cleaner,
                 movie: str = "movie") -> None:
    for person_params in customers:
        person = Customer(person_params["name"],
                          person_params["food"])

        CinemaBar.sell_product(person, person.food)

    cinema = CinemaHall(hall_number)
    cinema.movie_session(movie_name=movie,
                         customers=customers,
                         cleaning_staff=cleaner)
