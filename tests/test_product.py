from unittest.mock import patch

import pytest

from src.product import Product


def test_product(product_1):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 10


def test_product_init_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)


def test_new_product_class_method(product_dict):
    product = Product.new_product(product_dict)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "Описание продукта"
    assert product.price == 205000.0
    assert product.quantity == 5


def test_existing_product_class_method(product_dict, product_list):
    product = Product.new_product(product_dict, product_list)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 205000.0
    assert product.quantity == 15


def test_invalid_data_product_class_method(invalid_data):
    with pytest.raises(ValueError, match="Ошибка в структуре данных продукта"):
        Product.new_product(invalid_data)


def test_price_property(product_1, product_2):
    assert product_1.price == 180000.0
    assert product_2.price == 210000.0


@patch("builtins.input")
@pytest.mark.parametrize(
    "new_price, expected, user_answer", [(185000.0, 185000.0, "Y"), (50.0, 50.0, "Y"), (30.0, 180000.0, "answer")]
)
def test_price_setter(mock_input, new_price, expected, user_answer, product_1):
    mock_input.return_value = user_answer
    product_1.price = new_price
    assert product_1.price == expected


def test_price_setter_negative(capsys, product_1):
    product_1.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" == captured.out.split("\n")[1]


def test_str_product(product_1):
    assert str(product_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"


def test_add_product(product_1, product_2):
    assert product_1 + product_2 == 5580000.0


def test_add_product_negative(product_1, category):
    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        product_1 + 35000
