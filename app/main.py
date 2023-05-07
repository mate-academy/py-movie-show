from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_ins = [Customer(_["name"], _["food"]) for _ in customers]
    cinema_hall_ins = CinemaHall(hall_number)
    cleaner_ins = Cleaner(cleaner)
    for customer in customer_ins:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall_ins.movie_session(movie, customer_ins, cleaner_ins)
