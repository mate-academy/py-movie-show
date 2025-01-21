from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int, cleaner_name: str,
                 movie: str) -> str:
    result = []

    for customer in customers:
        result.append(f'Cinema bar sold {customer["food"]} to '
                      f'{customer["name"]}.\n')

    result.append(f'"{movie}" started in hall number '
                  f'{hall_number}.\n')

    for customer in customers:
        result.append(f'{customer["name"]} is watching "{movie}".\n')

    result.append(f'"{movie}" ended in hall number {hall_number}.\n')

    result.append(f'Cleaner {cleaner_name} is cleaning hall number '
                  f'{hall_number}.\n')

    return ''.join(result)
