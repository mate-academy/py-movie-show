from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    instance_customer = [Customer(cust.get("name"), cust.get("food"))
                         for cust in customers]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    instance_cleaner = Cleaner(cleaner)

    for cust in instance_customer:
        cinema_bar.sell_product(cust.food, cust)

    cinema_hall.movie_session(movie, instance_customer, instance_cleaner)
