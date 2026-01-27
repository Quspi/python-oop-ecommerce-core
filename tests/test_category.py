import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.exceptions import ZeroQuantityError


def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_empty_category(empty_category):
    assert len(empty_category.products) == 0

    assert Category.product_count == 0


def test_category_add_product(empty_category, product_1):
    empty_category.add_product(product_1)
    assert Category.product_count == 1
    assert product_1.name in empty_category.products


def test_category_add_product_negative(empty_category, category):
    with pytest.raises(TypeError, match="Добавлять можно только объекты Product или его наследников"):
        empty_category.add_product(category)


def test_category_add_product_zero_quantity(empty_category, product_1):
    product_1.quantity = 0
    with pytest.raises(ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"):
        empty_category.add_product(product_1)


def test_category_product_property(category):
    assert (
        category.products
        == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 10 шт.\nIphone 15, 210000.0 руб. Остаток: 18 шт.\n"
    )


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 28 шт."


def test_category_product_list_property(category, product_list):
    result = category.product_list
    assert result == product_list
    assert len(result) == 2


def test_category_iterator(category_iterator):
    iterator = iter(category_iterator)
    assert isinstance(iterator, CategoryIterator)
    assert iterator.index == 0
    assert next(iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(iterator).name == "Iphone 15"
    with pytest.raises(StopIteration):
        next(iterator)


def test_category_get_average_price(category):
    assert category.get_average_price() == 195000.0


def test_empty_category_get_average_price(empty_category):
    assert empty_category.get_average_price() == 0
