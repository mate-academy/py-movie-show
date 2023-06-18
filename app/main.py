from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customers_mod = []
    for elem in customers:
        temp = Customer(elem["name"], elem["food"])
        customers_mod.append(temp)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for client in customers_mod:
        cinema_bar.sell_product(client.food, client)

    cinema_hall.movie_session(movie, customers_mod, cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")



















