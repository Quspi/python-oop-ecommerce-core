import pytest


def test_order_init(empty_order):
    assert empty_order.order_id == 1
    assert empty_order.total_price == 0
    assert empty_order.product is None
    assert empty_order.quantity == 1


def test_order_str(empty_order, product_1):
    empty_order.add_product(product_1)
    assert str(empty_order) == "ID заказа: 2, к оплате: 180000.0 руб."


def test_order_add_product(empty_order, product_2):
    empty_order.add_product(product_2)
    assert empty_order.product == product_2
    assert empty_order.total_price == 210000.0


def test_add_second_product_raises_error(empty_order, product_1, product_2):
    empty_order.add_product(product_1)
    with pytest.raises(ValueError, match="В заказе может быть только один товар"):
        empty_order.add_product(product_2)


def test_order_quantity_exceeds_product_stock_raises_error(order_with_excessive_quantity, product_1):
    with pytest.raises(ValueError, match="Количество в заказе не может быть больше чем есть в магазине"):
        order_with_excessive_quantity.add_product(product_1)
