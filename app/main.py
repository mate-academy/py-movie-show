from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.visitor.customer import Customer
from app.visitor.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer_data in customers:
        customer_instance = Customer(name=customer_data["name"],
                                     food=customer_data["food"])
        cinema_bar.sell_product(customer=customer_instance,
                                product=customer_instance.food)

    cinema_hall.movie_session(movie_name=movie,
                              customers=[Customer(**customer)
                                         for customer in customers],
                              cleaning_staff=cleaner_instance)
    cleaner_instance.clean_hall(hall_number=hall_number)
