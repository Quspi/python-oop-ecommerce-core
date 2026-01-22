from __future__ import annotations


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
    def new_product(cls, product: dict) -> Product:
        """Метод для создания объекта Product из словаря."""
        try:
            return cls(**product)
        except TypeError:
            raise ValueError("Ошибка в структуре данных продукта")
