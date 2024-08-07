from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    list_of_people_instances = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    for pers in list_of_people_instances:
        bar_instance.sell_product(pers.food, pers)
    hall_instance.movie_session(
        movie, list_of_people_instances, cleaner_instance
    )
