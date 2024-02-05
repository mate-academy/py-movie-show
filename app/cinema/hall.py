from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: "Cleaner") -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        # Use customers directly as they are instances of Customer
        customer_instances = customers

        # Call watch_movie method for each customer
        for customer in customer_instances:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        # Call clean_hall method for the cleaning staff
        cleaning_staff.clean_hall(hall_number=self.number)
