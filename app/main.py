from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: CinemaHall,
    cleaner: Cleaner,
    movie: str
) -> None:

    customer_instances = []
    for customer in customers:
        customer_instances.append(Customer(**customer))

    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_bar_instance = CinemaBar()

    for customer in customer_instances:
        cinema_bar_instance.sell_product(customer.food, customer)
    hall_instance.movie_session(movie, customer_instances, cleaner_instance)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"},
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
        movie=movie
    )
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.
