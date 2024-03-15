from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    customers_instances = [Customer(name=customer_info["name"], food=customer_info["food"],) for customer_info in customers]

    for customer in customers_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)
        customer.watch_movie(movie)

    cinema_hall.movie_session(movie_name=movie, customers=customers_instances, cleaning_staff=cleaner)
