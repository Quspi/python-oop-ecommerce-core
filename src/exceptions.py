from typing import Any


class ZeroQuantityError(Exception):
    """Исключение при добавлении товара с нулевым количеством."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = args[0] if args else "Нельзя добавить нулевое количество"

    def __str__(self) -> str:
        """Возвращает сообщение об ошибке."""
        return self.message
