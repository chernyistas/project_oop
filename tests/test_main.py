from main import Category, Product

def test_product_init(product1, product2, product3):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14

def test_product_types(product1):
    assert isinstance(product1.name, str)
    assert isinstance(product1.description, str)
    assert isinstance(product1.price, float)
    assert isinstance(product1.quantity, int)

# def test_product_count_increment():
#     Category.category_count = 0
#     Category.product_count = 0
#
#     products_1 = [
#         Product("Product 1", "Desc 1", 100.0, 1),
#         Product("Product 2", "Desc 2", 200.0, 2),
#     ]
#     products_2 = [
#         Product("Product 3", "Desc 3", 300.0, 3),
#     ]
#
#     c1 = Category("Смартфоны", "Описание", products_1)
#     c2 = Category("Планшеты", "Описание", products_2)
#
#     assert Category.product_count == 3

# def test_category_count_increment():
#     # Сброс счетчика перед тестом
#     Category.category_count = 0
#     Category.product_count = 0
#
#     c1 = Category("Смартфоны", "Описание", [])
#     c2 = Category("Планшеты", "Описание", [])
#
#     assert Category.category_count == 2

# def test_product_count_with_empty_category():
#     Category.category_count = 0
#     Category.product_count = 0
#
#     c1 = Category("Пустая", "Нет продуктов", [])
#
#     assert Category.category_count == 1
#     assert Category.product_count == 0

def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3

    assert category1.category_count == 1
    assert category1.product_count == 3
