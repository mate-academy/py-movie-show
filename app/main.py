from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    hall = CinemaHall(hall_number)
    worker = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    [cinema_bar.sell_product(client, client.food) for client in clients]
    hall.movie_session(movie, clients, worker)
