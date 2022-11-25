class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
<<<<<<< HEAD
        print(f'{self.name} is watching "{movie}".')
=======
        print(f'{self.name} is watching \"{movie}\".')
>>>>>>> 8a0cf225de1c1d9d1123ba0233a2f852bd01be29
