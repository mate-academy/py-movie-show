from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    customers_objs = []
    for customer in customers:
        customer_obj = Customer(customer.get("name"), customer.get("food"))
        cinema_bar.sell_product(customer_obj.food, customer_obj)
        customers_objs.append(Customer(name=customer["name"],
                                       food=customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_objs, cleaner)
