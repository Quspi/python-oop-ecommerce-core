import json
from unittest.mock import mock_open, patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, load_json


@patch("os.path.exists")
def test_load_json(mock_os):
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data='[{"name": "test"}]')):
        result = load_json("fake_path")
        assert result == [{"name": "test"}]


@patch("os.path.exists")
def test_invalid_path(mock_os):
    mock_os.return_value = False
    with pytest.raises(FileNotFoundError, match="Файл invalid_path не найден или удален"):
        load_json("invalid_path")


@patch("os.path.exists")
def test_invalid_json(mock_os):
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data="{invalid_data")):
        with pytest.raises(json.JSONDecodeError):
            load_json("invalid_json")


def test_create_objects_from_json(json_data):
    result = create_objects_from_json(json_data)

    for category in result:
        assert isinstance(category, Category)

        products_str = category.products
        assert isinstance(products_str, str)
        assert len(products_str) > 0

    assert "100.0" in result[0].products
    assert result[0].name == "Смартфоны"


def test_invalid_data_create_objects_from_json(invalid_data):
    with pytest.raises(KeyError):
        create_objects_from_json(invalid_data)
