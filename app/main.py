from __future__ import annotations

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
    cinema_hall_instance = CinemaHall(hall_number)

    for customer in customers:
        CinemaBar.sell_product(
            customer=Customer(
                name=customer["name"],
                food=customer["food"]
            ),
            product=Customer(
                name=customer["name"],
                food=customer["food"]
            ).food
        )

    cinema_hall_instance.movie_session(
        movie,
        [
            Customer(
                name=customer["name"],
                food=customer["food"]
            )
            for customer in customers
        ],
        Cleaner(cleaner)
    )
