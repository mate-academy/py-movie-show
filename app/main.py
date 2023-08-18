from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie: str
) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for custom in customers:
        customer = Customer(name=custom["name"], food=custom["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer[i] for i in customers],
        cleaning_staff=cleaner
    )
