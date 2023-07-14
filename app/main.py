from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        CinemaBar.sell_product(customer=customer.get("name"), product=customer.get("food"))
    cinema_hall_instance = CinemaHall(hall_number)
    cinema_hall_instance.movie_session(cleaning_stuff=cleaner, customers=customers, movie_name=movie)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
