import sys
sys.path.append("D:/python_work/Mate Academy/py-cinema-visit/app/people")

from customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
