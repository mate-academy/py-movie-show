from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    list_of_customers = []
    for one_cust in customers:
        list_of_customers.append(
            Customer(one_cust.get("name"), one_cust.get("food"))
        )
    for one_cast in list_of_customers:
        cinema_bar.sell_product(one_cast.food, one_cast)
    cinema_hall.movie_session(movie, list_of_customers, cinema_cleaner)
