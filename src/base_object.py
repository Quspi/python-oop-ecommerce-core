from abc import ABC, abstractmethod

from src.product import Product


class BaseObject(ABC):
    """Абстрактный базовый класс для объектов, работающих с продуктами."""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализирует объект."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        ...

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """Добавляет продукт в объект."""
        ...
