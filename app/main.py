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
    # write you code here
    CinemaBar()
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)

    ch = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    ch.movie_session(customers=customers, cleaning_staff=cl, movie_name=movie)
