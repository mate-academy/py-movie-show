from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaning_staff)

    customers_list = []
    for customer_info in customers:
        customer = Customer(name=customer_info["name"], food=customer_info["food"])
        cinema_bar.sell_product(product=customer.food, customer=customer)
        customers_list.append(customer)

    cinema_hall.movie_session(movie_name=movie_name, customers=customers_list, cleaning_staff=cleaner)
