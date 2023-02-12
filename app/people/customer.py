class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __getitem__(self, item: str) -> None:
        return self.__dict__[item]

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
