# Ядро интернет-магазина на Python (ООП)

## Оглавление

- [Технологии](#технологии)
- [Функциональность](#функциональность)
- [Установка](#установка)
- [Пример использования](#пример-использования)
- [Тестирование](#тестирование)
- [Лицензия](#лицензия)
- [Автор](#автор)

## Технологии
- Python 3.12
- Pytest (тестирование)

## Функциональность

### Реализовано
- Класс Product: Моделирует товар с атрибутами: название, описание, цена, количество.

- Класс Category: Моделирует категорию товаров, содержит список товаров. Автоматически ведёт подсчёт категорий и товаров.

- Загрузка данных: Функции load_json и create_objects_from_json для инициализации объектов из JSON-файла.

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
from src.category import Category
from src.utils import load_json, create_objects_from_json

# Создание товаров вручную
phone = Product("iPhone", "Смартфон", 999.99, 10)
laptop = Product("MacBook", "Ноутбук", 1999.99, 5)

# Создание категории
electronics = Category("Электроника", "Техника", [phone, laptop])

print(electronics.name)  # Электроника
print(len(electronics.products))  # 2

# Загрузка из JSON
data = load_json("data/products.json")
categories = create_objects_from_json(data)
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