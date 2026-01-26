class MixinProductLog:
    """Миксин для логирования создания объектов Product."""

    def __init__(self) -> None:
        """Выводит repr объекта после инициализации."""
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта с его атрибутами."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
