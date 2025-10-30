import json
import os
from typing import Any

from main import Category, Product


def read_json(path: str) -> list[dict[str, Any]]:
    """Читает и парсит JSON-файл, возвращая список словарей."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise TypeError(f"Data in {path} must be a list")

    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Each item in data must be a dict")
    return data


def create_objects_from_json(json_data: list) -> list:
    """Преобразует список словарей (данные из JSON) в объекты Category и Product."""
    new_categories = []
    for cat in json_data:
        products = []
        for prod in cat["products"]:
            product = Product(
                name=prod["name"],
                description=prod.get("description", ""),
                price=prod.get("price", 0),
                quantity=prod.get("quantity", 0),
            )
            products.append(product)
        category = Category(name=cat["name"], description=cat.get("description", ""), products=products)
        new_categories.append(category)
    return new_categories
