from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_objs = list()
    for costumer in customers:
        new_costumer = Customer(costumer["name"], costumer["food"])
        customers_objs.append(new_costumer)

        CinemaBar.sell_product(new_costumer, new_costumer.food)

    cleaner = Cleaner(cleaner)
    new_hall = CinemaHall(hall_number)
    new_hall.movie_session(movie, customers_objs, cleaner)
