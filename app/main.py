from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = []
    for cust in customers:
        visitors.append(Customer(cust["name"], cust["food"]))

    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for vis in visitors:
        cinema_bar.sell_product(vis.food, vis)

    hall.movie_session(movie, visitors, clean)
