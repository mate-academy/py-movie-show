# write your imports here
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # write you code here
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    # Create a CinemaBar instance and sell food to the customers
    cinema_bar = CinemaBar()
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    # Create a CinemaHall instance
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              cleaning_staff=Cleaner(cleaner),
                              customers=customer_instances)
    # Create the cleaner_instance
    cleaner_instance = Cleaner(cleaner)
