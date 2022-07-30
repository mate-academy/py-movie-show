
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    cinema_bar = CinemaBar()
    for index, customer in enumerate(customers):
        customer_instance = Customer(customer["name"], customer["food"])
        customers_list.append(customer_instance)
        cinema_bar.sell_product(customer["food"], customers_list[index])

    hall_number_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    hall_number_instance.movie_session(movie, customers_list, cleaner_instance)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5,
             cleaner="Anna",
             movie="Madagascar")
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
