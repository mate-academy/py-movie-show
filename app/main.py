from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_customers = []
    for elements in customers:
        CinemaBar.sell_product(
            customer=Customer(elements["name"], elements["food"]),
            product=elements["food"])
        list_customers.append(Customer(elements["name"], elements["food"]))
    CinemaHall.movie_session(self=CinemaHall(hall_number),
                             movie_name=movie,
                             customers=list_customers,
                             cleaning_staff=Cleaner(cleaner))
