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
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_list = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    [
        bar.sell_product(customer=customer, product=customer.food)
        for customer in customers_list
    ]
    hall.movie_session(movie, customers_list, cleaning_staff)
