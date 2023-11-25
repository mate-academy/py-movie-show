# write your imports here
from app.peaple.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str):
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    for i in customers:
        cs = Customer(i["name"], i["food"])
        cb.sell_product(customer=cs.name, product=cs.food)
    ch.movie_session(movie=movie, customers=customers, cleaning_staff=cleaner)
