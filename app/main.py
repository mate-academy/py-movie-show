from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    custom_instance = [Customer(customer["name"],
                                customer["food"])
                       for customer in customers]
    cinema_bar_inst = CinemaBar()
    cinema_hall_inst = CinemaHall(hall_number)
    cleaner_inst_inst = Cleaner(cleaner)
    for instance in custom_instance:
        cinema_bar_inst.sell_product(instance.food, instance)
    cinema_hall_inst.movie_session(movie, custom_instance, cleaner_inst_inst)
