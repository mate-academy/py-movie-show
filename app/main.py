from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaner)

    for person in customer_list:
        cinema_bar.sell_product(person.food, person)

    cinema_hall.movie_session(movie, customer_list, cinema_staff)
