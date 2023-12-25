from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    new_customer = []
    for client in customers:
        new_customer.append(Customer(client["name"], client["food"]))
        CinemaBar.sell_product(Customer(client["name"], client["food"]),
                               client["food"])
    cleaning = Cleaner(cleaner)
    class_hall = CinemaHall(hall_number)
    class_hall.movie_session(movie, new_customer, cleaning)
