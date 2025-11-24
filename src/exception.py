from typing import Optional


class ZeroProductCount(Exception):
    """Класс исключения, который отвечает за обработку событий добавления товара с нулевым количеством"""

    def __init__(self, message: Optional[str] = None) -> None:
        """Конструктор класса исключения."""
        super().__init__(message)
