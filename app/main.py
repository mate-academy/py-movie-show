from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from typing import List, Dict


def cinema_visit(
        customers: List[Dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    persons_inst = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        persons_inst.append(person)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for person in persons_inst:
        cinema_bar.sell_product(person, person.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=persons_inst,
        cleaning_staff=cleaner
    )
