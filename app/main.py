from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    all_visitors = [Customer(every_customer["name"], every_customer["food"])
                    for every_customer in customers]
    for visitor in all_visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    current_cleaner = Cleaner(cleaner)
    current_hall = CinemaHall(hall_number)
    current_hall.movie_session(movie, all_visitors, current_cleaner)
