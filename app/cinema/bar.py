


class CinemaBar:

    @staticmethod
    def sell_product(product, customer):


        print(f'Cinema bar sold {product} to {customer}.')

# Внутри этого модуля создайте CinemaBar класс, описывающий работу кинобара.
# Этот класс должен иметь только один статический метод sell_product, который принимает product имя продукта,
# который хочет клиент, и customer экземпляр Customer, означающий клиента.
# Этот метод печатает, какой продукт и кому продали кинотеатры.
# cb = CinemaBar()
# customer = Customer("Bob", "popcorn")
# cb.sell_product(customer=customer, product=customer.food)
# # Cinema bar sold popcorn to Bob.