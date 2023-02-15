from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    all_customers = []
    staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers:
        all_customers.append(Customer(
            name=customer["name"],
            food=customer["food"]
        ))
    for person in all_customers:
        CinemaBar.sell_product(
            customer=person,
            product=person.food
        )
    CinemaHall.movie_session(self=hall,
                             movie_name=movie,
                             customers=all_customers,
                             cleaning_staff=staff)
    pass
