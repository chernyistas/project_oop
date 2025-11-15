from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        """Абстрактный метод класса для создания нового продукта"""
        pass


class BaseOrderCategory(ABC):

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        pass
