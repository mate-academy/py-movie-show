from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        if type(customers[0]) is dict:
            customers_list = []
            for customer in customers:
                customer = Customer(
                    name=customer["name"],
                    food=customer["food"]
                )
                customers_list.append(customer)
        else:
            customers_list = customers

        for customer in customers_list:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
