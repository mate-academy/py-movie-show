from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, list_of_customers, cleaner_staff)
