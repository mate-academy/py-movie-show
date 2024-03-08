from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()

    customer_instances = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)
        customer_instances.append(customer)

    cinema_hall = CinemaHall(number=hall_number)

    cleaner = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie, customers=customer_instances, cleaning_staff=cleaner
    )

# Example usage:


customers_data = [
    {"name": "John", "food": "Popcorn"},
    {"name": "Alice", "food": "Soda"},
    # Add more customer data as needed
]

hall_number = 1
cleaner_name = "Bob"
movie_name = "Movie Title"

cinema_visit(
    customers=customers_data,
    hall_number=hall_number,
    cleaner=cleaner_name,
    movie=movie_name
)
