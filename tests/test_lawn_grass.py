import pytest


def test_lawn_grass_init(lawn_grass_1):
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Трава для газона"
    assert lawn_grass_1.price == 50.0
    assert lawn_grass_1.quantity == 100
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == 14
    assert lawn_grass_1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 8750.0


def test_lawn_grass_add_negative(lawn_grass_1, product_1):
    with pytest.raises(TypeError, match="Складывать можно только объекты LawnGrass."):
        lawn_grass_1 + product_1
