from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    for man in customers:
        CinemaBar.sell_product(Customer(man["name"], man["food"]),
                               man["food"])
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(
        movie,
        [Customer(name=customer["name"], food=customer["food"])
         for customer in customers],
        clean)
