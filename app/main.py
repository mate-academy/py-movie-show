from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    new_bar = CinemaBar()
    for i in range(len(customers)):
        list_of_customers.append(Customer(
            name=customers[i]["name"],
            food=customers[i]["food"])
        )
        new_bar.sell_product(product=customers[i]["food"],
                             customer=list_of_customers[i])
    hall = CinemaHall(number=hall_number)
    clean = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=clean
    )
