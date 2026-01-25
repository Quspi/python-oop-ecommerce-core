import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "iPhone 15"
    assert smartphone_1.description == "Смартфон"
    assert smartphone_1.price == 1000.00
    assert smartphone_1.quantity == 10
    assert smartphone_1.efficiency == 95
    assert smartphone_1.model == "15 Pro"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Black"


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 13000.0


def test_smartphone_add_negative(smartphone_1, product_1):
    with pytest.raises(TypeError, match="Складывать можно только объекты Smartphone."):
        smartphone_1 + product_1
