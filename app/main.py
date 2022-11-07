from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall_number = CinemaHall(number=hall_number)
    for customer_dict in customers:
        customer = Customer(name=customer_dict["name"],
                            food=customer_dict["food"])
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall.movie_session(hall_number, movie, customers, cleaner)
