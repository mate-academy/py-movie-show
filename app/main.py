import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @staticmethod
    def from_birth_year(name: str, birth_year: int):
        return Person(name, datetime.date.today().year - birth_year)

    def display(self):
        print(f"{self.name} (age: {self.age}). "
              f"Is adult: {Person.is_adult(self.age)}")

    @staticmethod
    def is_adult(age):
        return age >= 18
