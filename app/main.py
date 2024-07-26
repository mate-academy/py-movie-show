from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner_instance = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customer_instances = [
        Customer(cust["name"], cust["food"])
        for cust in customers
    ]
    bar_cinema = CinemaBar()

    for customer in customer_instances:
        bar_cinema.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie, customer_instances, cleaner_instance)
