from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_object = [Customer(name=customer["name"], food=customer["food"])
                        for customer in customers if customer]
    for customer in customers_object:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_object, cleaner)
