from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:
    hall = CinemaHall(hall_number)
    hall_bar = CinemaBar()
    hall_cleaner = Cleaner(cleaner)

    hall_customers = [Customer(person["name"], person["food"])
                      for person in customers]

    for person in hall_customers:
        hall_bar.sell_product(person, person.food)

    hall.movie_session(movie, hall_customers, hall_cleaner)
