from cinema import bar
from cinema import hall
from people import cinema_staff
from people import customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    cinema_hall = hall.CinemaHall(hall_number)  # Create an instance of the hall
    cinema_bar = bar.CinemaBar()  # Create an instance of the bar
    cleaner_instance = cinema_staff.Cleaner(cleaner)  # Create an instance of the cleaner

    customer_instances = [customer.Customer(cust['name'], cust['food']) for cust in customers]

    for cust_instance in customer_instances:
        cinema_bar.sell_product(cust_instance.name, cust_instance.food)

    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
