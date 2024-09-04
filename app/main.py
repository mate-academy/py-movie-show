from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    # Create instances of customers
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # Create instance of CinemaBar
    cinema_bar = CinemaBar()

    # Sell products to customers
    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    # Create instance of CinemaHall
    cinema_hall = CinemaHall(hall_number)

    # Create instance of Cleaner
    cleaner_instance = Cleaner(name=cleaner)

    # Start movie session
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
