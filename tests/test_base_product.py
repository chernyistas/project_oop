from typing import Any

from src.base_product import BaseOrderCategory, BaseProduct


class Product1(BaseProduct):
    @classmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        return cls()


def test_base_product() -> None:
    """Тестирует метод new_product класса Product1"""
    instance = Product1.new_product()
    assert isinstance(instance, Product1)


class Category1(BaseOrderCategory):

    def __str__(self) -> str:
        """Возвращает строковое представление категории"""
        return "Category1"


def test_base_order_category() -> None:
    """Тестирует строковое представление для Category1"""
    instance = Category1()
    assert str(instance) == "Category1"
