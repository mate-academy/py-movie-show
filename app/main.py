from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(custom: list, hall_num: int, cleanr: str, movie: str) -> None:
    customer_list = []
    for customer in custom:
        customer_list.append(Customer(customer["name"], customer["food"]))

    for person in customer_list:
        CinemaBar.sell_product(person.food, person)

    new_hall_number = CinemaHall(hall_num)
    new_cleaner = Cleaner(cleanr)
    new_hall_number.movie_session(movie, customer_list, new_cleaner)
