from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    movie_enjoyers_inst = [
        Customer(movie_enjoyer["name"], movie_enjoyer["food"])
        for movie_enjoyer in customers
    ]
    cleaner_inst = Cleaner(cleaner)
    hall_init = CinemaHall(hall_number)
    for movie_enjoyer in movie_enjoyers_inst:
        CinemaBar.sell_product(movie_enjoyer.food, movie_enjoyer)
    hall_init.movie_session(movie, movie_enjoyers_inst, cleaner_inst)
