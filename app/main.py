from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:

    customer_objs = []
    outputs = []
    for customer in customers:
        outputs.append(
            f"Cinema bar sold {customer['food']} to {customer['name']}."
        )
        customer_obj = Customer(customer["name"], customer["food"])
        customer_objs.append(customer_obj)

    outputs.append(f'"{movie}" started in hall number {hall_number}.')
    for customer_obj in customer_objs:
        outputs.append(f'{customer_obj.name} is watching "{movie}".')
    outputs.append(f'"{movie}" ended.')
    outputs.append(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")

    for output in outputs:
        print(output)
