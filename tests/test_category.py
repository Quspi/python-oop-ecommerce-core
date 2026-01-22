from src.category import Category


def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_empty_category(empty_category):
    assert len(empty_category.products) == 0

    assert Category.product_count == 0
