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
    customer_instance = [
        Customer(person.get("name"), person.get("food"))
        for person in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    for person in customer_instance:
        CinemaBar.sell_product(person.food, person)
    cinema_hall.movie_session(movie, customer_instance, Cleaner(cleaner))
