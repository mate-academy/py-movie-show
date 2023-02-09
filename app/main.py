from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = []
    for elem in customers:
        clients.append(Customer(
            name=elem.get("name"),
            food=elem.get("food")
        ))
    for client in clients:
        CinemaBar.sell_product(customer=client, product=client.food)
    CinemaHall(hall_number).movie_session(movie, clients, Cleaner(cleaner))
