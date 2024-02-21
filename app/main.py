
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: Cleaner, movie: str) -> None:
    # Create Customers instances
    customer_instances = [
        Customer(name=customer["name"],
                 food=customer["food"]) for customer in customers]
    # Create instances of CinemaBar, CinemaHall, and Cleaner
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)

    # Sell food at the cinema bar
    for customer_instance in customer_instances:
        cinema_bar.sell_product(
            customer=customer_instance, product=customer_instance.food)

    # Run movie session
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances, cleaning_staff=cinema_cleaner)
