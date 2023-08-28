from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_list_instance = []
    for person in customers:
        customers_person_instance = Customer(person.get("name"), person.get("food"))
        customers_list_instance.append(customers_person_instance)

    c_hall_inst = CinemaHall(hall_number)
    bar = CinemaBar()

    cleaner_instance = Cleaner(cleaner)

    for person in customers_list_instance:
        bar.sell_product(person, person.food)

    c_hall_inst.movie_session(movie, customers_list_instance, cleaner_instance)
