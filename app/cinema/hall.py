from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers: list, cleaner):
        print(f'{movie_name} started in hall number {self.number}.')

        for cust in customers:
            cust.watch_movie(movie_name)

        print(f'{movie_name} ended.')
        Cleaner.clean_hall(cleaner, self.number)










#hall.py- внутри этого модуля создайте CinemaHall класс,
# описывающий действия во время киносеанса.
# Его конструктор берет и сохраняет number- номер зала в кинотеатре.
# Этот класс должен иметь только один метод movie_session,
# который принимает movie_name, customers- список клиентов ( Customer экземпляры), cleaning_staff- уборщик ( Cleaner экземпляр).
# Этот метод выводит информацию о начале фильма,
# вызывает метод клиентов watch_movie,
# выводит информацию о конце фильма,
# вызывает метод очистки clean_hall.