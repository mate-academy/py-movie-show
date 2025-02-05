from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):

    customer_instances = [Customer(name=cust['name'], food=cust['food']) for cust in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)