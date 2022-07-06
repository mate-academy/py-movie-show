class Customer:
    cust_name_food = []

    def __init__(self, name, food):
        self.name = name
        self.food = food


    def watch_movie(self, movie):
        print(f'{self.name} is watching {movie}.')

# customer.py- внутри этого модуля создайте Customer класс,
# его конструктор берет и хранит name, food- еду, которую клиент хочет купить в баре кинотеатра.
# Этот класс должен иметь только один метод watch_movie,
# этот метод принимает movie и печатает то, что клиент смотрит фильм.
# bob = Customer(name="Bob", food="popcorn")
# bob.watch_movie(movie="Madagascar")
# # Bob is watching "Madagascar".
