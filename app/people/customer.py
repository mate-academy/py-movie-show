class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    @staticmethod
    def watch_movie(movie: str) -> None:
        print(f"{Customer} is watching {movie}")
