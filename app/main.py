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
    cinema_bar: CinemaBar = CinemaBar()
    cinema_hall: CinemaHall = CinemaHall(number=hall_number)
    cleaner: Cleaner = Cleaner(name=cleaner)

    for customer_data in customers:
        customer: Customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        cinema_bar.sell_product(
            customer=customer,
            product=customer.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[
            Customer(
                name=customer_data["name"],
                food=customer_data["food"]
            ) for customer_data in customers
        ],
        cleaning_staff=cleaner
    )
