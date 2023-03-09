from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer = [Customer(person["name"], person["food"])
                for person in customers]
    cleaner_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for person in customer:
        CinemaBar.sell_product(person, person.food)

    cinema_hall.movie_session(movie, customer, cleaner_staff)
