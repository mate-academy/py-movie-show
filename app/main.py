from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import Any


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> Any:
    # Создаём экземпляр CinemaHall и Cleaner
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    # Создаём экземпляры Customer и продаём каждому еду в баре
    customer_instances = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_instances.append(customer)
    # Проводим киносеанс и вызываем уборку зала
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
