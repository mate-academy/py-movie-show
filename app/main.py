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
    for value in customers:
        customers_list.append(Customer(name=value["name"], food=value["food"]))
    cinema_bar = CinemaBar()
    for value in customers_list:
        cinema_bar.sell_product(value.food, value)
    hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    hall.movie_session(movie, customers_list, cinema_cleaner)
