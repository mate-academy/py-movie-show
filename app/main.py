from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    # Create CinemaBar instance
    cb = CinemaBar()

    # Sell products to customers
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        cb.sell_product(customer=customer, product=customer.food)

    # Create Cleaner instance
    cleaning_staff = Cleaner(name=cleaner)

    # Create CinemaHall instance
    ch = CinemaHall(number=hall_number)

    # Start movie session
    ch.movie_session(
        movie_name=movie,
        customers=[
            Customer(name=customer_data["name"], food=customer_data["food"])
            for customer_data in customers
        ],
        cleaning_staff=cleaning_staff
    )
