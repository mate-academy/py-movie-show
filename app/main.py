from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for client in customers:
        new_customer = Customer(name=client.get("name"), food=client.get("food"))



customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
