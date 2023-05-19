from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    bar_as_obj = CinemaBar()
    hall_as_obj = CinemaHall(hall_number)
    cleaner_as_obj = Cleaner(cleaner)
    customers_as_objs = []
    for person in customers:
        customer_obj = Customer(
            person["name"],
            person["food"]
        )
        customers_as_objs.append(customer_obj)
        bar_as_obj.sell_product(
            product=person["food"],
            customer=customer_obj)
    hall_as_obj.movie_session(
        movie_name=movie,
        customers=customers_as_objs,
        cleaning_staff=cleaner_as_obj
    )
