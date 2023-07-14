from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    for customer in customers:
        CinemaBar.sell_product(customer=Customer(customer.get("name"),
                                                 customer.get("food")),
                               product=customer.get("food"))

    cleaner = Cleaner(cleaner)

    cinema_hall_instance = CinemaHall(hall_number)
    customers_new = []
    for human in customers:
        customers_new.append(Customer(human.get("name"), human.get("food")))
    cinema_hall_instance.movie_session(cleaning_staff=cleaner,
                                       customers=customers_new,
                                       movie_name=movie)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5,
             cleaner="Anna",
             movie="Madagascar")
