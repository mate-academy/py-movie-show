from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: str, hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    cinema_bar = CinemaBar()

    customer_instances = [Customer(
        name=customer["name"], food=customer["food"])
        for customer in customers]

    for customer in customer_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(number=hall_number)

    cleaner = Cleaner(name=cleaner_name)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances,
                              cleaning_staff=cleaner)
