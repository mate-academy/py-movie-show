from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: str):
        print(f'{movie_name} started in hall number {self.number}.')

        number = 0
        for _ in customers:
            customer_name = customers[number]['name']
            customer_food = customers[number]['food']
            customer = Customer(customer_name, customer_food)
            customer.watch_movie(movie_name)
            number += 1

        print(f'{movie_name} ended.')

        clean = Cleaner(cleaning_staff)
        clean.clean_hall(self.number)
