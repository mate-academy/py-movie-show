class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')

    def get(self, text: str) -> str:
        if text == "name":
            return self.name
        elif text == "food":
            return self.food
