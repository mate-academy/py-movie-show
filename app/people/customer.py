class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> str:
        return f"{self.name} is watching \"{movie}\"."
