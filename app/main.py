from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    customer_list = []
    for customer in customers:
        cust_class = Customer(customer.get("name"), customer.get("food"))
        cinema_bar.sell_product(cust_class.food, cust_class)
        customer_list.append(cust_class)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cleaner)
