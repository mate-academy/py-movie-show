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
    for person in customers:
        Customer(person.get("name"), person.get("food"))
    cinema_hall = CinemaHall(hall_number)
    CinemaBar()
    first_cleaner = Cleaner(cleaner)
    for person in range(-len(customers), 0):
        CinemaBar.sell_product(
            Customer.people[person],
            Customer.people[person].food
        )
    CinemaHall.movie_session(
        cinema_hall,
        movie,
        Customer.people[-len(customers):],
        first_cleaner
    )
