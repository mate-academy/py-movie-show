from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = [Customer(customer.get("name"),
                                    customer.get("food"))
                           for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers_instances:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_instances, cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 4
cleaner_name = "Anna"
movie = "I'm Robot"
cinema_visit(customers=customers,
             hall_number=4,
             cleaner="Anna",
             movie="I'm Robot")
