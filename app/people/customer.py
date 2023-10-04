class Customer:
    def __init__(self, name: dict | str, food: str = None) -> None:

        if isinstance(name, dict):
            self.name = name["name"]
            self.food = name["food"]
        else:
            self.name = name
            self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
