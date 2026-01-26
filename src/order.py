from typing import Optional

from src.base_object import BaseObject
from src.product import Product


class Order(BaseObject):
    """Класс, представляющий заказ на один товар."""

    __order_id: int = 1

    def __init__(self, quantity: int = 1) -> None:
        """Инициализирует новый заказ с уникальным ID."""
        self.quantity: int = quantity
        self.total_price: float = 0
        self.product: Optional[Product] = None
        self.order_id: int = Order.__order_id

        Order.__order_id += 1

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"ID заказа: {self.order_id}, к оплате: {self.total_price}руб."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в заказ и рассчитывает финальную стоимость."""
        if self.product is None:
            self.product = product
            if product.quantity <= self.quantity:
                self.total_price = self.quantity * product.price
            else:
                raise ValueError("Количество в заказе не может быть больше чем есть в магазине")
        else:
            raise ValueError("В заказе может быть только один товар")
