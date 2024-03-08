from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner_name: str, movie: str
) -> None:
    # Input validation
    if not isinstance(customers, list):
        raise TypeError("customers must be a list of dictionaries")
    if not all(isinstance(customer, dict) for customer in customers):
        raise TypeError("each customer must be a dictionary")
    if not isinstance(hall_number, int):
        raise TypeError("hall_number must be an integer")
    if not isinstance(cleaner_name, str):
        raise TypeError("cleaner_name must be a string")
    if not isinstance(movie, str):
        raise TypeError("movie must be a string")

    # Proceed with the logic only if inputs are valid
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    customer_instances = [
        Customer(info["name"], info["food"])
        for info in customers
        if "name" in info and "food" in info
    ]

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
