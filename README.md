# Ядро интернет-магазина на Python (ООП)

## Оглавление

1. [Технологии](#технологии)
2. [Функциональность](#функциональность)
3. [Поддерживаемые форматы данных](#поддерживаемые-форматы-данных)
4. [Установка](#установка)
5. [Пример использования](#использование)
6. [Тестирование](#тестирование)
7. [Лицензия](#лицензия)
8. [Автор](#автор)

## Технологии
- Python 3.12
- Pytest (тестирование)
- Poetry (для управления зависимостями и виртуальным окружением)

## Функциональность

### Реализовано
**Базовые классы**:
- `Product`: товар с названием, описанием, ценой, количеством.
- `Category`: категория товаров с подсчётом.
- `CategoryIterator`: итератор по товарам категории.

**Наследники Product**:
- `Smartphone`: добавляет производительность, модель, память, цвет.
- `LawnGrass`: добавляет страну-производителя, срок прорастания, цвет.

**Утилиты**:
- Загрузка данных из JSON (`load_json`, `create_objects_from_json`).

**Методы**:
- `Category.add_product`: добавляет товар (проверяет `isinstance(product, Product)`).
- `Product.__add__`: складывает стоимость двух товаров.
- `Smartphone.__add__` / `LawnGrass.__add__`: складывают только объекты одного класса.

**Приватные атрибуты и свойства**
- `Product.__price`: приватная цена с геттером/сеттером `price`.
- `Category.__products`: приватный список товаров. Свойство products возвращает строку вида `"Название, X руб. Остаток: Y шт.\n"`.

**Валидация и логика**:
- Сеттер `price` проверяет: цена > 0. При понижении цены запрашивает подтверждение (`Y`).
- Класс-метод `Product.new_product` создаёт товар из словаря, объединяет дубликаты (суммирует количество, берёт max цену).

## Поддерживаемые форматы данных
- JSON

## Установка
```
# Клонирование репозитория
git clone https://github.com/Quspi/python-oop-ecommerce-core

# Установка зависимостей
poetry install
```

## Использование

```python
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category
from src.utils import load_json, create_objects_from_json

# 1. Базовое использование
phone = Product("iPhone", "Смартфон", 999.99, 10)
laptop = Product("MacBook", "Ноутбук", 1999.99, 5)
electronics = Category("Электроника", "Техника", [phone, laptop])

print(electronics.name)  # Электроника
print(electronics.products)
# Вывод:
# iPhone, 999.99 руб. Остаток: 10 шт.
# MacBook, 1999.99 руб. Остаток: 5 шт.

# 2. Загрузка из JSON
categories = create_objects_from_json(load_json("data/products.json"))

# 3. Работа с ценой (геттер/сеттер)
product = Product("Товар", "...", 100.0, 5)
product.price = 150.0  # Установка новой цены
# product.price = -10   # Выведет: "Цена не должна быть нулевая или отрицательная"
# product.price = 50    # Запросит подтверждение (цена снижается)

# 4. Класс-метод new_product с объединением дубликатов
existing = [Product("Телефон", "...", 500.0, 2)]
new_data = {"name": "Телефон", "description": "...", "price": 550.0, "quantity": 3}
updated = Product.new_product(new_data, existing)
print(f"Обновлённый товар: количество={updated.quantity}, цена={updated.price}")
# Обновлённый товар: количество=5, цена=550.0

# 5. Добавление товара в категорию
electronics.add_product(Product("Наушники", "...", 200.0, 8))

# 6. Новые классы товаров
smartphone = Smartphone("Galaxy S24", "Смартфон", 899.99, 15, 
                       efficiency=95, model="S24", memory=256, color="Black")
grass = LawnGrass("Газонная трава", "Для газона", 50.0, 100,
                  country="Россия", germination_period=14, color="Зеленый")

garden = Category("Сад", "Товары для сада", [grass])

# 7. Сложение товаров
total_smartphones = smartphone + smartphone  # ОК
# total_mixed = smartphone + grass          # Вызовет TypeError
```

## Тестирование

Проект покрыт юнит-тестами Pytest. Для их запуска выполните команды:
```
# Запуск всех тестов
pytest

# Запуск с отчетом о покрытии в консоли
pytest --cov=src

# Генерация HTML отчета о покрытии (будет создана папка htmlcov/)
pytest --cov=src --cov-report=html
```

## Лицензия
Этот проект распространяется под лицензией MIT.

## Автор
**Oleg Tamanov**

Email: olegtamanov@gmail.com