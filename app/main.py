from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_bar = CinemaBar
    for customer in customers:
        new_customer = Customer(customer.get("name"), customer.get("food"))
        new_bar.sell_product(new_customer.food, new_customer)
    new_session = CinemaHall(hall_number)
    list_of_customers = [Customer(name=customer["name"],
                                  food=customer["food"])
                         for customer in customers]
    cleaner = Cleaner(cleaner)
    new_session.movie_session(movie, list_of_customers, cleaner)
