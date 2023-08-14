from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int or str,
        cleaning_staff: str,
        movie_name: str or int
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaning_staff)

    customer_instances = [
        Customer(
            cust["name"],
            cust["food"]
        )
        for cust in customers
    ]

    for cust_instance in customer_instances:
        cinema_bar.sell_product(cust_instance, cust_instance.food)

    cinema_hall.movie_session(
        movie_name,
        customer_instances,
        cleaner_instance
    )
