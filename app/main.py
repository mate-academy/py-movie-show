# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    cs_ = [Customer(name=cs_p["name"], food=cs_p["food"])
           for cs_p in customers]
    for i in customers:
        cs = Customer(i["name"], i["food"])
        cb.sell_product(customer=cs, product=cs.food)
    ch.movie_session(movie=movie, customers=cs_, cleaning_staff=cl)

# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
