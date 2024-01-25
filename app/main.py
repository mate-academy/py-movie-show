from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    
    customer_object = []
    for customer_info in customers:
        customer = Customer(customer_info['name'], customer_info['food'])
        cinema_bar.sell_product(customer.food, customer)
        customer_objects.append(customer)

    cinema_hall.movie_session(movie_name, customer_objects, cleaner)

