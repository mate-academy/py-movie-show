from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int, cinema_staff: str):
        self.number = number
        self.cinema_staff = cinema_staff

    def movie_session1(self, movie_name: str) -> str:
        print(f'"{movie_name}" started in hall number {self.number}.')


    def movie_session(self, movie_name: str) -> str:
         print(f'"{movie_name}" ended.')


    if __name__ == "__main__":
        def movie_session2(self, movie_name: str) -> str:
            Customer.watch_movie()
            print(f'Cleaner "{self.cinema_staff.name}" is cleaning hall number {self.cinema_staff.clean_hall.number}.')

def test_cinema_hall_constructor():
    cinema_staff = [Cleaner('John Doe', 'Manager'), Cleaner('Jane Smith', 'Cashier')]
    ch = CinemaHall(number=6, cinema_staff=cinema_staff)
