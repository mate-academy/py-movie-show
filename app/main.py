from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    customer_instances = [
        Customer(name=cust["name"],
                 food=cust["food"])
        for cust in customers
    ]
    for cust in customer_instances:
        cinema_bar.sell_product(product=cust.food, customer=cust)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customer_instances,
                              cleaning_staff=cleaner_instance
                              )
