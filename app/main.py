from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie: str,
) -> None:
    customers_classed = []
    for cust in customers:
        person = Customer(name=cust["name"], food=cust["food"])
        cb = CinemaBar()
        cb.sell_product(customer=person, product=person.food)
        customers_classed.append(person)

    num = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaning_staff)
    num.movie_session(
        movie_name=movie,
        customers=customers_classed,
        cleaning_stuff=cleaner)


# if __name__ == "__main__":
#     customers = [{'name': 'Bob', 'food': 'popcorn'}]
#     hall_number = 1
#     cleaner_name = "Anna"
#     movie = "Tenet"
#     cinema_visit(
#         customers=customers,
#         hall_number=hall_number,
#         cleaning_staff=cleaner_name,
#         movie=movie)
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.
