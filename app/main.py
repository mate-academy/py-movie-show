from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:

    customers_list = [Customer(name= customer["name"], food= customer["food"]) for customer in customers]
    for customer in customers_list:
        CinemaBar.sell_product(customer= customer, product= customer.food)

    cleaner_inst = Cleaner(cleaner)
    hall = CinemaHall(number= hall_number)
    hall.movie_session(movie_name= movie, customers= customers_list, cleaner= cleaner_inst)

