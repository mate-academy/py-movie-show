# write your imports here
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    # write you code here
    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customers,
        cleaning_staff=cleaner
    )
