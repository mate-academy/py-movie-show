from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    customer_list = [Customer(**person) for person in customers]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for person in customer_list:
        CinemaBar.sell_product(person.food, person)

    hall.movie_session(movie, customer_list, cleaner)
