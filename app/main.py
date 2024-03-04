from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.cinema.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie_name: str) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner()

    for customer_info in customers:
        customer = Customer(customer_info['name'], customer_info['food'])
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie_name,
        [Customer(customer['name'],
                  customer['food']) for customer in customers],
        cinema_cleaner
    )

    cinema_cleaner.clean_hall(cleaner_name, hall_number)
