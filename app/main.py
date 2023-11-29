# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    c_bar = CinemaBar()
    c_hall = CinemaHall(hall_number)
    c_cleaner = Cleaner(cleaner)
    c_customers = [Customer(name=customer["name"], food=customer["food"])
                   for customer in customers]
    for customer in customers:
        custmr = Customer(customer["name"], customer["food"])
        c_bar.sell_product(customer=custmr, product=custmr.food)
    c_hall.movie_session(movie=movie,
                         customers=c_customers,
                         cleaning_staff=c_cleaner
                         )
