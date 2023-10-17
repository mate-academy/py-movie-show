from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    persons_inst = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        persons_inst.append(person)

    cinema_hall_inst = CinemaHall(number=hall_number)
    cinema_bar_inst = CinemaBar()
    cleaner_inst = Cleaner(name=cleaner)

    for person in persons_inst:
        cinema_bar_inst.sell_product(person, person.food)

    cinema_hall_inst.movie_session(
        movie_name=movie,
        customers=persons_inst,
        cleaning_staff=cleaner_inst
    )
