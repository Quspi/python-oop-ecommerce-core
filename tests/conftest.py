import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 18)


@pytest.fixture
def category(product_1, product_2):
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product_1, product_2],
    )


@pytest.fixture
def empty_category():
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Телевизоры",
        "Современные телевизоры",
        [],
    )


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [{"name": "Samsung", "description": "Описание продукта", "price": 100.0, "quantity": 5}],
        }
    ]


@pytest.fixture
def invalid_data():
    return [{"name": "Категория без товаров"}]


@pytest.fixture
def product_dict():
    return {"name": "Samsung Galaxy C23 Ultra", "description": "Описание продукта", "price": 205000.0, "quantity": 5}


@pytest.fixture
def product_list(product_1, product_2):
    return [product_1, product_2]


@pytest.fixture
def category_iterator(category):
    return CategoryIterator(category)


@pytest.fixture
def smartphone_1():
    return Smartphone("iPhone 15", "Смартфон", 1000.00, 10, 95, "15 Pro", 256, "Black")


@pytest.fixture
def smartphone_2():
    return Smartphone("iPhone 12", "Смартфон", 300.00, 10, 75, "12 Pro", 512, "Black")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Трава для газона", 50.0, 100, "Россия", 14, "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Трава спортивная", "Для стадионов", 75.0, 50, "Германия", 10, "Темно-зеленый")


@pytest.fixture
def empty_order():
    return Order()


@pytest.fixture
def order_with_excessive_quantity():
    return Order(1000)
