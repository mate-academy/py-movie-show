from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cust_list = []
    for cust in customers:
        cust1 = Customer(cust.get("name"), cust.get("food"))
        cust_list.append(cust1)

    cinemahall = CinemaHall(hall_number)
    cinemabar = CinemaBar
    cleaner1 = Cleaner(cleaner)

    for cust in cust_list:
        cinemabar.sell_product(cust.food, cust)

    cinemahall.movie_session(movie, cust_list, cleaner1)
