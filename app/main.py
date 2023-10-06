# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    clients = [Customer(customer.get("name"),
                        customer.get("food"))
               for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for client in clients:
        cinema_bar.sell_product(client.food, client)
    cinema_hall.movie_session(movie, clients, cleaner)
