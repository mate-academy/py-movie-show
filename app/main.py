from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # Створюємо об'єкти для кожного клієнта
    customer_instances = []
    for customer_info in customers:
        customer = Customer(name=customer_info["name"], food=customer_info["food"])
        customer_instances.append(customer)

    # Продаємо продукти кожному клієнту через CinemaBar
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створюємо об'єкт CinemaHall для зазначеного номера залу
    hall = CinemaHall(number=hall_number)

    # Розпочинаємо сеанс фільму
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=Cleaner(name=cleaner))
