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
    customers_list = []
    for people in customers:
        customers_list.append(Customer(
            name=people["name"],
            food=people["food"]
        ))

    for cust in customers_list:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    clean_staff = Cleaner(name=cleaner)
    new_hall = CinemaHall(number=hall_number)
    CinemaHall.movie_session(
        self=new_hall,
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=clean_staff
    )
