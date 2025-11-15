import pytest

from src.models import Product


def test_print_mixin(capsys: "pytest.CaptureFixture[str]") -> None:
    """Тестирует вывод информации о продукте при создании экземпляров класса Product"""

    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
