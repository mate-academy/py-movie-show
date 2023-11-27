from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_the_customers = [
        Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        for customer_dict in customers
    ]
    current_bar = CinemaBar()
    for customer_instance in list_of_the_customers:
        current_bar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )
    hall = CinemaHall(number=hall_number)
    current_cleaner = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_of_the_customers,
        cleaning_staff=current_cleaner
    )
