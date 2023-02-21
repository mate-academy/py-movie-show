from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    new_customers_list = []
    for customer in customers:
        new_customers_list.append(Customer(customer["name"], customer["food"]))
    for new_cinema_bar in new_customers_list:
        CinemaBar.sell_product(new_cinema_bar, new_cinema_bar.food)
    cleaner_name = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, new_customers_list, cleaner_name)
