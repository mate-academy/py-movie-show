from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers:  list,
        hall_number: int,
        cleaner: str
):
    now_in_hall = [
        Customer(client["name"], client["food"]) for client in customers
    ]

    hall = CinemaHall(hall_number)

    for customer in now_in_hall:
        CinemaBar(customer, customer.food).sell_product(customer, customer.food)

    stuff = Cleaner(cleaner)

    hall.movie_session(movie, now_in_hall, stuff)

    Cleaner(cleaner).clean_hall(hall.number)


customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
]

cleaner_name = "Anna"
hall_number = 5
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="I'm robot")
