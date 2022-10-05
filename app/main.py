from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for client in customers:
        CinemaBar.sell_product(Customer(client['name'], client['food']),
                               client['food'])
    CinemaHall(hall_number).movie_session(movie,
                                          [Customer(a['name'], a['food'])
                                           for a in customers],
                                          Cleaner(cleaner)
                                          )
