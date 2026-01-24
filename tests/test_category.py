from src.category import Category


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
