from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cb = CinemaBar()
    #
    #

    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        cb.sell_product(customer=customer, product=customer.food)

    cleaner = Cleaner(name=cleaner_name)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name,
        [Customer(customer_data["name"],
                  customer_data["food"]) for customer_data in customers],
        cleaner)
