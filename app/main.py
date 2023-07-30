from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for i in range(len(customers)):
        customers[i] = Customer(customers[i]["name"], customers[i]["food"])
        cinema_bar.sell_product(
            customers[i].food,
            customers[i]
        )

    cinema_hall.movie_session(movie, customers, cleaner)
