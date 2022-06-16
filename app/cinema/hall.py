class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for i in customers:
            print(f'{i.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(f'Cleaner {cleaning_staff.name} '
              f'is cleaning hall number {self.number}.')
