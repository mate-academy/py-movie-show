# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    # write you code here
    customer_instances = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    for i in customers:
        customer_instances.append(Customer(i["name"], i["food"]))

    for i in customer_instances:
        cinema_bar.sell_product(i.food, i)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
