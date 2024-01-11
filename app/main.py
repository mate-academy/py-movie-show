from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_list = list()

    for person in customers:
        customers_list.append(Customer(person["name"], person["food"]))

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for buyer in customers_list:
        cinema_bar.sell_product(buyer, buyer.food)

    hall.movie_session(movie, customers_list, cleaner)
