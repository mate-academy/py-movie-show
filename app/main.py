from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    normalized_customers = []

    for customer in customers:
        normalized_customers.append(
            Customer(
                customer["name"],
                customer["food"]
            )
        )

    cinema_hall = CinemaHall(hall_number)

    normalized_cleaner = Cleaner(cleaner)

    for customer in normalized_customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, normalized_customers, normalized_cleaner)
