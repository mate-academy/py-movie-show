from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    res_customers = []
    for customer in customers:
        res_customers.append(Customer(name=customer["name"],
                                      food=customer["food"]))
    res_cinema_hall = CinemaHall(hall_number)
    res_cleaning_staff = Cleaner(cleaner)

    for customer in res_customers:
        CinemaBar.sell_product(customer.food, customer)

    res_cinema_hall.movie_session(movie, res_customers, res_cleaning_staff)
