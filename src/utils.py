import json
import os

from src.category import Category
from src.product import Product


def load_json(path: str) -> list[dict]:
    """Функция для загрузки данных из json-файла."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл {path} не найден или удален")

    with open(path, "r", encoding="utf-8") as file:
        data: list[dict] = json.load(file)

    return data


def create_objects_from_json(data: list[dict]) -> list[Category]:
    """Создает объекты Category и Product из данных JSON."""
    categories = []

    for category in data:
        products = []

        for product in category["products"]:
            products.append(Product(**product))

        category["products"] = products
        categories.append(Category(**category))

    return categories
