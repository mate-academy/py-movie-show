from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaning_stuff = Cleaner(cleaner)
    for customer in customers_obj:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_obj, cleaning_stuff)
