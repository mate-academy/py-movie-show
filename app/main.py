from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_list = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner_name)
