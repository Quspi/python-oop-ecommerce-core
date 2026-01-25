from src.product import Product


class Category:
    """Класс для представления категории товара."""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Возвращает строку: 'название категории, количество продуктов:
        X шт.', где X - сумма quantity всех товаров категории."""
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в список продуктов категории."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с информацией о всех товарах категории, используя их строковое представление."""
        products_info = ""
        for product in self.__products:
            products_info += str(product)
        return products_info

    @property
    def product_list(self) -> list[Product]:
        """Возвращает список товаров категории."""
        return self.__products
