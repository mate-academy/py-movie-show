from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)
    clients = []
    for customer in customers:
        client = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(client, client.food)
        clients.append(client)
    hall.movie_session(movie, clients, cleaner_person)
