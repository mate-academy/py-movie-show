from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie_title: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    cinema_bar = CinemaBar()
    visitors = []

    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        visitors.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie_title, visitors, cleaner)
