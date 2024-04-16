from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    people = [
        Customer(el["name"], el["food"]) for el in customers
    ]
    movie_hall = CinemaHall(hall_number)
    movie_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    for el in people:
        movie_bar.sell_product(el, el.food)
    movie_hall.movie_session(movie, people, cinema_cleaner)
