# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    # write you code here
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    visitors = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(visitor.food, visitor)
        visitors.append(visitor)

    hall.movie_session(movie_name, visitors, cleaner)
    # cleaner.clean_hall(hall_number)


watchers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
cinema_visit(watchers, 5, "Anna", "Madagascar")
