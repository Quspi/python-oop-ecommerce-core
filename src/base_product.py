from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        ...

    @abstractmethod
    def __add__(self, other: "Product") -> float:
        """Возвращает суммарную стоимость товара self и other на основе их цены и количества."""
        ...
