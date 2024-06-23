from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)

    customers_as_classes = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_as_class = Cleaner(cleaner)

    for customer in customers_as_classes:
        cb.sell_product(customer=customer, product=customer.food)

    ch.movie_session(movie_name=movie,
                     customers=customers_as_classes,
                     cleaning_staff=cleaner_as_class)


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
