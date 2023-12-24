from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers_like_class = []
    for customer in customers:
        list_of_customers_like_class.append(Customer
                                            (customer.get("name"),
                                             customer.get("food"))
                                            )
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in list_of_customers_like_class:
        product = customer.food
        CinemaBar.sell_product(customer, product)

    hall.movie_session(movie, list_of_customers_like_class, cleaning_staff)
