from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customers_instance_list = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    bar_of_cinema = CinemaBar()
    for customer in customers_instance_list:
        bar_of_cinema.sell_product(
            product=customer.food,
            customer=customer
        )
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instance_list,
        cleaning_staff=cleaner
    )
