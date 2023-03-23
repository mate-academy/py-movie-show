from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))
