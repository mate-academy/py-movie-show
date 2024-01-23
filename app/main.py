# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # Create instances
    customers_instances = [
        Customer(name=cust["name"],
                 food=cust["food"]
                 ) for cust in customers]
    cb = CinemaBar()
    ch = CinemaHall(number=hall_number)

    cleaner = Cleaner(name=cleaner)

    # Sell food to customers
    for customer in customers_instances:
        cb.sell_product(product=customer.food, customer=customer)

    # Start movie session
    ch.movie_session(movie_name=movie,
                     customers=customers_instances,
                     cleaning_staff=cleaner)
