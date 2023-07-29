# Cinema visit

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

You have opened your own cinema. To have a better idea 
of what's going on in the cinema 
you decided to keep a record of events in the cinema.
For this purpose you have to create such modules:

1. In directory `app` create package `cinema`. In this
package create modules:  
   - `bar.py` - inside this module create `CinemaBar`
   class that describes work of cinema bar.
   This class should have only one static method `sell_product`,
   that takes `product` - name of the product that customer wants
   and `customer` - `Customer` instance, that means customer.
   This method prints what product and to whom cinema sold.
   
   ```python
   cb = CinemaBar()
   customer = Customer("Bob", "popcorn")
   cb.sell_product(customer=customer, product=customer.food)
   # Cinema bar sold popcorn to Bob.
   ```

   - `hall.py` - inside this module create `CinemaHall`
   class that describes actions during the movie session. Its
   `__init__` method takes and stores `number` - number of the hall
   in cinema.
   This class should have only one method `movie_session`, that
   takes `movie_name`, `customers` - list of a customers
   (`Customer` instances), `cleaning_staff` - cleaner (`Cleaner` 
   instance). This method prints about movie start, calls 
   customers method `watch_movie`, prints about movie end,
   calls cleaner method `clean_hall`.
2. In directory `app` create package `people`. In this package
   create modules:
   - `customer.py` - inside this module create `Customer` class,
   its `__init__` method takes and stores `name`, `food` - food that 
   customer wants to buy in cinema bar. 
   This class should have only one method `watch_movie`, this 
   method takes `movie` and prints what movie customer is watching.
   
   ```python
   bob = Customer(name="Bob", food="popcorn")
   bob.watch_movie(movie="Madagascar")
   # Bob is watching "Madagascar".
   ```
   
   - `cinema_staff` - inside this module create `Cleaner` class,
   its `__init__` method takes and stores `name`. 
   This class should have only one method `clean_hall`, this method
   takes `hall_number` - number of hall that cleaner have to clean and
   prints that cleaner is cleaning that hall.

   ```python
   anna = Cleaner(name="Anna")
   anna.clean_hall(hall_number=5)
   # Cleaner Anna is cleaning hall number 5.
   ```

In the module `main.py` you have to import all this classes. Classes
should be imported by absolute path, that starts with 'app.' with 
keyword 'from'. Write a
function `cinema_visit` that takes `movie_name`, `customers` - a list 
of customers, elements are dicts with 'name' and desired 'food' of a 
customer, `hall_number` - number of the hall in cinema, 
`cleaning_staff` - name of the cleaner, that will clean the
hall after movie session.

This function should make `Customers` instances, instance of `CinemaHall`
and `CinemaBar`, instance of `Cleaner`. First, cinema bar should sell food to
customers, then cinema hall should make a movie session and finally cleaner
cleans cinema hall.

Example: 
```python
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
```













Ви відкрили власний кінотеатр. Щоб мати кращу ідею
про те, що відбувається в кінотеатрі
ви вирішили вести облік подій в кінотеатрі.
Для цього необхідно створити такі модулі:

1. У каталозі `app` створіть пакет `cinema`. У цьому
модулі створення пакетів:
   - `bar.py` - всередині цього модуля створіть `CinemaBar`
   клас, що описує роботу кінобару.
   Цей клас повинен мати лише один статичний метод `sell_product`,
   який приймає `product` - назву продукту, який хоче клієнт
   і `customer` - екземпляр `Customer`, тобто клієнт.
   Цей метод друкує, який продукт і кому продав кінотеатр.

cb = CinemaBar()
   customer = Customer("Bob", "popcorn")
   cb.sell_product(customer=customer, product=customer.food)
   # Cinema bar sold popcorn to Bob.
   ```





- `hall.py` - всередині цього модуля створіть `CinemaHall`
   клас, який описує дії під час кіносеансу. Його
   Метод `__init__` приймає і зберігає `number` - номер залу
   в кіно.
   Цей клас повинен мати лише один метод `movie_session`, тобто
   приймає `movie_name`, `customers` - список клієнтів
   (примірники `Customer`), `cleaning_staff` - прибиральник (`Cleaner`
   екземпляр). Цей метод друкує про початок фільму, дзвінки
   клієнтський метод `watch_movie`, друкує інформацію про кінець фільму,
   викликає метод очищення `clean_hall`.
2. У каталозі `app` створіть пакет `people`. У цьому пакеті
   створити модулі:
   - `customer.py` - всередині цього модуля створіть клас `Customer`,
   його метод `__init__` приймає та зберігає `name`, `food` - їжу, яка
   клієнт хоче купити в барі кіно.
   Цей клас повинен мати лише один метод `watch_movie`, this
   метод бере `кіно` і друкує те, який фільм дивиться клієнт.
   
   ```пітон
   bob = Клієнт (ім'я="Боб", їжа="попкорн")
   bob.watch_movie(фільм="Мадагаскар")
   # Боб дивиться "Мадагаскар".
   ```
   
   - `cinema_staff` - всередині цього модуля створіть клас `Cleaner`,
   його метод `__init__` приймає та зберігає `name`.
   Цей клас повинен мати лише один метод `clean_hall`, цей метод
   приймає `номер_залу` - номер залу, який має прибрати прибиральник
   друкує, що прибиральник прибирає той зал.







У модулі `main.py` вам потрібно імпортувати всі ці класи. Заняття
слід імпортувати за абсолютним шляхом, який починається з "app". з
ключове слово "від". Написати
функція `cinema_visit`, яка приймає `movie_name`, `customers` - список
клієнтів, елементи є диктовками з «ім'ям» і бажаною «їжею» a
замовник, `номер_залу` - номер залу в кінотеатрі,
`cleaning_staff` - ім'я прибиральника, який буде прибирати
зал після кіносеансу.

Ця функція має створювати екземпляри `Клієнти`, екземпляр `Кінозал`
і `CinemaBar`, екземпляр `Cleaner`. По-перше, кіно-бар повинен продавати їжу
клієнтів, то кінозал повинен зробити кіносеанс і, нарешті, чистіше
прибирає кінозал.