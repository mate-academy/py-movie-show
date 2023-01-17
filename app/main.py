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

    person_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    for person in person_list:
        CinemaBar.sell_product(product=person.food, customer=person)

    cleaner = Cleaner(cleaner)
    current_hall = CinemaHall(hall_number)
    current_hall.movie_session(
        movie_session=movie,
        customers=person_list,
        cleaning_staff=cleaner
    )
