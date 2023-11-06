from __future__ import annotations

import app.people.customer as people_c


class CinemaBar:
    @staticmethod
    def sell_product(customer: people_c.Customer, product: str) -> None:
        return print(f"Cinema bar sold {product} to {customer.name}.")
