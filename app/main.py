from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall1 = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    customers_resutl = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        customers_resutl.append(customer)
        cinema_bar.sell_product(customer.food, customer)
    hall1.movie_session(movie, customers_resutl, cleaner1)
