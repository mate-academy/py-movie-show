from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cleaner_inst = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    clients = []
    for customer in customers:
        clients.append(Customer(customer["name"], customer["food"]))
    for client in clients:
        CinemaBar.sell_product(client.food, client)
    hall.movie_session(movie, clients, cleaner_inst)
