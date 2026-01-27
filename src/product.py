from __future__ import annotations

from typing import Optional

from src.base_product import BaseProduct
from src.mixin_product_log import MixinProductLog


class Product(MixinProductLog, BaseProduct):
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Возвращает строковое представление товара в формате: 'название, цена руб. Остаток: количество шт.'"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: Product) -> float:
        """Возвращает суммарную стоимость товара self и other на основе их цены и количества."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product: dict, existing_products: Optional[list[Product]] = None) -> Product:
        """
        Создаёт объект Product из словаря.
        Если передан список existing_products, ищет товар с таким же именем.
        При нахождении дубликата увеличивает его количество и выбирает максимальную цену.
        Возвращает существующий (обновлённый) или новый объект Product.
        """
        try:
            new_product = cls(**product)
        except TypeError:
            raise ValueError("Ошибка в структуре данных продукта")

        if existing_products is not None:
            for existing_product in existing_products:
                if existing_product.name == new_product.name:
                    existing_product.quantity += new_product.quantity
                    existing_product.price = max(existing_product.price, new_product.price)
                    return existing_product

        return new_product

    @property
    def price(self) -> float:
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Устанавливает новую цену товара.
        Если цена <= 0, выводит предупреждение и не изменяет цену.
        Если новая цена ниже текущей, запрашивает подтверждение через ввод 'Y'.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_answer = input("Новая цена ниже текущей, для подтверждения введите `Y`")
                if user_answer.upper() == "Y":
                    self.__price = new_price
            else:
                self.__price = new_price
