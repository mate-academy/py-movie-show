from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customer_list = []
    for client in customers:
        customer_sample = Customer(client["name"], client["food"])
        customer_list.append(customer_sample)
        CinemaBar.sell_product(customer=customer_sample,
                               product=client["food"])

    hall = CinemaHall(hall_number)
    cleaner_example = Cleaner(cleaner)
    hall.movie_session(customers=customer_list,
                       movie_name=movie,
                       cleaning_staff=cleaner_example)
