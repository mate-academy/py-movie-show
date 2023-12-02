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
    customers_list = []
    for inst in customers:
        customer_inst = Customer(inst["name"], inst["food"])
        customers_list.append(customer_inst)
    cinema_hall = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaner)
    for person in customers_list:
        CinemaBar.sell_product(person, person.food)
    cinema_hall.movie_session(movie, customers_list, cleaner_inst)
