import pytest

from src.category import Category
from src.product import Product


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
