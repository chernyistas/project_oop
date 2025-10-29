import pytest
from main import Product
from main import Category


@pytest.fixture()
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture()
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category1(product1, product2, product3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
