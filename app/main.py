from app.cinema.Bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    bar = CinemaBar()
    clean = Cleaner(cleaner)
    customer_cs = []
    for cust in customers:
        customer_cs.append(Customer(cust["name"], cust["food"]))
    for customer_new in customer_cs:
        bar.sell_product(customer_new.food, customer_new)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_cs, clean)


