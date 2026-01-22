from __future__ import annotations

from typing import Optional


class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

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
