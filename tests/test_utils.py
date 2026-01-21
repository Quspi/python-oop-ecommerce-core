import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_json


@patch("os.path.exists")
def test_load_json(mock_os):
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data='[{"name": "test"}]')):
        result = load_json("fake_path")
        assert result == [{"name": "test"}]


@patch("os.path.exists")
def test_invalid_path(mock_os):
    mock_os.return_value = False
    with pytest.raises(FileNotFoundError, match="Файл "):
        load_json("invalid_path")


@patch("os.path.exists")
def test_invalid_json(mock_os):
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data="{invalid_data")):
        with pytest.raises(json.JSONDecodeError):
            load_json("invalid_json")
