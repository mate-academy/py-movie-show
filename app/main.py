from cinema import bar, hall
from people import customer, cinema_staff


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str):
    new_customer = None
    for dict in customers:
        new_customer = customer.Customer(dict["name"], dict["food"])
        bar.CinemaBar.sell_product(new_customer.name, new_customer.food)
    hall.CinemaHall.movie_session(hall_number)
    cinema_staff.Cleaner(cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5, cleaner="Anna", movie="Madagascar")
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.