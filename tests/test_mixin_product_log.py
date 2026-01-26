from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_product_log(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 10)"

    Smartphone("iPhone 15", "Смартфон", 1000.00, 10, 95, "15 Pro", 256, "Black")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Smartphone(iPhone 15, Смартфон, 1000.0, 10)"

    LawnGrass("Газонная трава", "Трава для газона", 50.0, 100, "Россия", 14, "Зеленый")
    captured = capsys.readouterr()
    assert captured.out.strip() == "LawnGrass(Газонная трава, Трава для газона, 50.0, 100)"
