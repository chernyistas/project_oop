from unittest.mock import mock_open, patch

import pytest

from src.utils import create_objects_from_json, read_json


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Смартфоны", ' '"description": "desc", "products": []}]',
)
def test_read_json_success(mock_file: str) -> None:
    data = read_json("fake_path.json")
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    assert data[0]["name"] == "Смартфоны"


@patch("builtins.open", new_callable=mock_open, read_data='{"wrong": "format"}')
def test_read_json_not_list(mock_file: str) -> None:
    with pytest.raises(TypeError):
        read_json("fake_path.json")


@patch("builtins.open", new_callable=mock_open, read_data='["string"]')
def test_read_json_item_not_dict(mock_file: str) -> None:
    with pytest.raises(TypeError):
        read_json("fake_path.json")


# Тесты для create_objects_from_json
def test_create_objects_from_json() -> None:
    json_data = [
        {
            "name": "Смартфоны",
            "description": "desc",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    categories = create_objects_from_json(json_data)
    assert len(categories) == 1
    cat = categories[0]
    assert cat.name == "Смартфоны"
    assert cat.description == "desc"
    assert len(cat.products) == 1
    prod = cat.products[0]
    assert prod.name == "Samsung Galaxy C23 Ultra"
    assert prod.price == 180000.0
    assert prod.quantity == 5
    assert prod.description == "256GB, Серый цвет, 200MP камера"
