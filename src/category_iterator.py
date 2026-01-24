from src.category import Category
from src.product import Product


class CategoryIterator:
    def __init__(self, category: Category):
        """Инициализирует итератор для перебора товаров категории."""
        self.category = category
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        """Сбрасывает индекс итератора и возвращает сам итератор."""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар из категории или вызывает StopIteration."""
        if self.index < len(self.category.product_list):
            product = self.category.product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
