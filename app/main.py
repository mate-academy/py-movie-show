from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    peoples_list = []
    for customer in customers:
        people = Customer(customer["name"], customer["food"])
        peoples_list.append(people)
        CinemaBar.sell_product(people.food, people)

    CinemaHall(hall_number).movie_session(
        movie,
        peoples_list,
        Cleaner(cleaner)
    )
