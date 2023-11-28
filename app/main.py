from app.cinema.bar import CinemaBar
from app.cinema.cinema_stuff import Cleaner
from app.cinema.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for index, value in enumerate(customers):
        customer = Customer(value["name"], value["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(value["food"], customer)
    hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
