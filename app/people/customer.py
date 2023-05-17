class Customer:
    def __init__(self, name: str, food: str) -> None:
        self._name = name
        self._food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self._name} is watching "{movie}".')

    @property
    def food(self) -> str:
        return self._food

    @property
    def name(self) -> str:
        return self._name
