from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> list:

    customers_list = [
        Customer(name=cust["name"], food=cust["food"]) for cust in customers
    ]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)

    for customer in customers_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cleaning = Cleaner(name=cleaner)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=cleaning)
