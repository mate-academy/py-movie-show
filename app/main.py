from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for cinema_customer in customers:
        cinema_customer = Customer(cinema_customer["name"],
                                   cinema_customer["food"])
        cinema_bar.sell_product(cinema_customer, cinema_customer.food)

    cinema_hall.movie_session(movie, customers, cinema_cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
