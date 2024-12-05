from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    # Ensure customers is a list of dictionaries
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"]) for customer in customers
    ]

    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)
