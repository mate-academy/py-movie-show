from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for customer_dict_elements in customers:
        customer = Customer(customer_dict_elements["name"],
                             customer_dict_elements["food"])
        customers_list.append(customer)    
    today_hall = CinemaHall(hall_number)
    today_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    today_hall.movie_session(movie, customers_list, cleaner)
