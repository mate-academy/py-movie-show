from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict] | list[Customer],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    for person in customers:
        if isinstance(person, dict):
            food, name = person['food'], person['name']
        if isinstance(person, Customer):
            food, name = person.food, person.name
        CinemaBar.sell_product(food, name)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name, customers, Cleaner(cleaning_staff))
