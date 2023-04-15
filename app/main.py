from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    for customer in customers:
        customer_obj = Customer(customer.get("name"), customer.get("food"))
        cinema_bar.sell_product(customer_obj.food, customer_obj)
    cinema_hall = CinemaHall(hall_number)
    customers_objs = [Customer(name=customer["name"],
                               food=customer["food"])
                      for customer in customers]
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_objs, cleaner)
