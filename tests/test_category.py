from src.category import Category


def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert (
        category.products
        == f"Название продукта, 180000.0 руб. Остаток: 10 шт.\nНазвание продукта, 210000.0 руб. Остаток: 18 шт.\n"
    )

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_empty_category(empty_category):
    assert len(empty_category.products) == 0

    assert Category.product_count == 0
