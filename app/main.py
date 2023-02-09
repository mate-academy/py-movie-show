from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    # make instances of Customers
    list_customers_ins = [(Customer(customer["name"], customer["food"]))
                          for customer in customers]

    cin_hall_ins = CinemaHall(hall_number)  # make instance of CinemaHall
    cin_bar_ins = CinemaBar()               # make instance of CinemaBar
    cleaner_ins = Cleaner(cleaner)          # make instance of Cleaner

    [cin_bar_ins.sell_product(customer.food, customer)
     for customer in list_customers_ins]   # cinema bar sell food to customers

    cin_hall_ins.movie_session(movie, list_customers_ins, cleaner_ins)
