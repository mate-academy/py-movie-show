from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cinema_bar = CinemaBar()
    curr_cleaner = Cleaner(cleaner)
    curr_hall = CinemaHall(hall_number)
    curr_customers = []
    for customer in customers:
        curr_customer = Customer(customer.get("name"), customer.get("food"))
        cinema_bar.sell_product(curr_customer, curr_customer.food)
        curr_customers.append(curr_customer)
    curr_hall.movie_session(movie, curr_customers, curr_cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5,
             cleaner="Anna", movie="Madagascar")
