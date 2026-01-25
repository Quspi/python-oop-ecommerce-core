from src.product import Product


class LawnGrass(Product):
    """Класс, представляющий товар 'Газонная трава'.
    Наследует атрибуты и методы от класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        """Инициализирует экземпляр класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> float:
        """Возвращает суммарную стоимость товаров LawnGrass на основе их цены и количества."""
        if type(other) is not LawnGrass:
            raise TypeError("Складывать можно только объекты LawnGrass.")
        return super().__add__(other)
