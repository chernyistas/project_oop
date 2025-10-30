from main import Category, Product


def test_product_init(product1: Product, product2: Product, product3: Product) -> None:
    """Проверяет правильную инициализацию объектов Product."""
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


def test_product_types(product1: Product) -> None:
    """Проверяет типы данных атрибутов объекта Product."""
    assert isinstance(product1.name, str)
    assert isinstance(product1.description, str)
    assert isinstance(product1.price, float)
    assert isinstance(product1.quantity, int)


def test_category_and_product_count(category1: Category, product4: Product) -> None:
    """Проверяет обновление счетчиков категорий и продуктов при создании новой категории."""
    Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_init(category1: Category, product1: Product, product2: Product, product3: Product) -> None:
    """Проверяет корректность инициализации объекта Category."""
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3

    assert category1.category_count == 1
    assert category1.product_count == 3
    assert category1.products == [product1, product2, product3]
