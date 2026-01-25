from src.product import Product


class Smartphone(Product):
    """Класс, представляющий товар 'Смартфон'.
    Наследует атрибуты и методы от класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: int,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализирует экземпляр класса Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Product) -> float:
        """Возвращает суммарную стоимость товаров Smartphone на основе их цены и количества."""
        if type(other) is not Smartphone:
            raise TypeError("Складывать можно только объекты Smartphone.")
        return super().__add__(other)
