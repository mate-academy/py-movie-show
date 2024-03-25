from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customers_list = []
    for cus in customers:
        customer = Customer(name=cus["name"], food=cus["food"])
        CinemaBar.sell_product(customer, customer.food)
        customers_list.append(customer)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
