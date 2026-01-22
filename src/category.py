from src.product import Product


class Category:
    """Класс для представления категории товара."""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в список продуктов категории."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
