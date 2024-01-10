from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    edited_customers = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        edited_customers.append(customer)

        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=edited_customers,
        cleaning_staff=cinema_cleaner
    )
