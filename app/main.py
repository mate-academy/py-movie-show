from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    hall = CinemaHall(hall_number)
    bar_func = CinemaBar()
    cleaning = Cleaner(cleaner)
    list_of_customer = []

    for bar_sell in customers:
        customer = Customer(bar_sell["name"], bar_sell["food"])
        list_of_customer.append(customer)
        bar_func.sell_product(product=bar_sell["food"], customer=customer)

    CinemaHall.movie_session(self=hall, movie_name=movie,
                             customers=list_of_customer,
                             cleaning_staff=cleaning)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5,
             cleaner="Anna", movie="Madagascar")
