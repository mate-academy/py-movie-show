from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> str:
    visitors = []
    for visitor in customers:
        visitors.append(Customer(visitor["name"], visitor["food"]))
    clean_hall = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for person in visitors:
        CinemaBar.sell_product(person, person.food)
    CinemaHall.movie_session(hall, movie, visitors, clean_hall)
