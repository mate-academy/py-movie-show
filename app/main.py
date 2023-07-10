from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_inst = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall_inst = CinemaHall(hall_number)
    bar_inst = CinemaBar()
    cleaner_inst = Cleaner(cleaner)

    for customer in customers_inst:
        bar_inst.sell_product(customer.food, customer)

    hall_inst.movie_session(movie, customers_inst, cleaner_inst)
