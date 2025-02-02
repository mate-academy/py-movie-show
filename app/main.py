from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 number: int,
                 cleaner: str,
                 movie: str):
    cinema_hall = CinemaHall(number)
    cleaning_staff = Cleaner(cleaner)
    customer_list = [Customer(customer["name"], customer["food"]) for customer in customers]
    customer_list.reverse()
    for customer in customer_list:
        CinemaBar.sell_product(customer)

    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
    pass
