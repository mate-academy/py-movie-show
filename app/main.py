from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for i in range(len(customers)):
        person = CinemaBar()
        customers[i] = Customer(customers[i]["name"], customers[i]["food"])
        person.sell_product(customers[i].food, customers[i])
    cinema_hall.movie_session(movie, customers, clean)
