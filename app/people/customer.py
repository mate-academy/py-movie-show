class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie):
        print(f"{self.name} is watching \"{movie}\".")


bob = Customer(name="Bob", food="popcorn")
bob.watch_movie(movie="Madagascar")
# Bob is watching "Madagascar".
