from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []
    for cust in customers:
        customer = Customer(cust.get("name"), cust["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, clean)
