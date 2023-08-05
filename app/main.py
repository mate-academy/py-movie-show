from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie_name: str,
        customers: list,
        hall_number: int,
        cleaning_staff: str
) -> None:
    # Create instances
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaning_staff)

    # Create customer instances
    customer_instances = [
        Customer(cust["name"], cust["food"]) for cust in customers
    ]

    # Sell food in the bar
    for cust_instance in customer_instances:
        cinema_bar.sell_product(cust_instance.name, cust_instance.food)

    # Start movie session
    cinema_hall.movie_session(movie_name, customer_instances, cleaner_instance)
