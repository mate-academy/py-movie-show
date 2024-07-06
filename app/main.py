from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie_name):
    customer_instances = [Customer(name=param['name'], food=param['food']) for param in customers]
    cinema_bar = CinemaBar()
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie_name=movie_name, customers=customer_instances, cleaning_staff=cleaning_staff)
