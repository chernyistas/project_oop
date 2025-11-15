import pytest

from src.models import Category, LawnGrass, Order, Product, ProductIterator, Smartphone


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
    assert Category.product_count == 34


def test_category_init(category1: Category, product1: Product, product2: Product, product3: Product) -> None:
    """Проверяет корректность инициализации объекта Category."""
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.product_list) == 3

    assert category1.category_count == 1
    assert category1.product_count == 27
    assert category1.product_list == [product1, product2, product3]


def test_create_new_product(data: dict) -> None:
    """Тест на создание нового продукта"""
    product = Product.new_product(data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_update_existing_product(data: dict) -> None:
    """Тест на обновления существующего продукта"""
    existing = [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 195000, 3)]
    update_product = Product.new_product(data, existing)

    assert update_product is existing[0]
    assert update_product.quantity == 8
    assert update_product.price == 195000


def test_update_existing_product_price_no_change(data: dict) -> None:
    """Тест на обновления продукта, когда новая цена меньше текущей."""
    existing = [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 3)]
    update_product = Product.new_product(data, existing)
    assert update_product.price == 180000


def test_price_getter_setter(data: dict) -> None:
    """Тест на геттер и сеттер для свойства price."""
    product = Product.new_product(data)
    assert product.price == 180000
    product.price = 160000
    assert product.price == 160000
    product.price = 0
    assert product.price == 0
    old_price = product.price
    product.price = -1
    assert product.price == old_price


def test_products_property(product1: Product, product2: Product, product3: Product) -> None:
    """Тест свойства products класса Category."""
    category = Category("Смартфоны", "Мобильные телефоны", [product1, product2, product3])

    expected = (
        "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.\n"
    )

    assert category.products == expected


def test_product_list_property(product1: Product, product2: Product, product3: Product) -> None:
    """Тест свойства product_list класса Category."""
    category = Category("Смартфоны", "Мобильные телефоны", [product1, product2, product3])
    result = category.product_list
    assert result == [product1, product2, product3]


def test_product_str(product1: Product, product2: Product, product3: Product) -> None:
    """Тест на строковое представление объекта Product"""
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    """Тест на проверку суммирования стоимости товаров двух объектов Product"""
    result = product1 + product2
    assert result == 2580000

    not_a_product = "not a product"
    with pytest.raises(TypeError):
        product1 + not_a_product


def test_category_str(category1: Category) -> None:
    """Тест на строковое представление объекта Category"""
    assert str(category1) == "Смартфоны, количество продуктов: 27"


def test_product_iterator(category1: Category) -> None:
    """Тест на итератор по списку продуктов категории"""
    iterator = ProductIterator(category1)
    assert str(next(iterator)) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."
    assert str(next(iterator)) == "Iphone 15, 210000 руб. Остаток: 8 шт."
    assert str(next(iterator)) == "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт."

    with pytest.raises(StopIteration):
        next(iterator)


def test_smartphone_init(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    """Тест на правильную инициализацию объектов Smartphone"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_lawngrass_init(grass1: LawnGrass, grass2: LawnGrass) -> None:
    """Тест на правильную инициализацию объектов LawnGrass"""

    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"

    assert grass2.name == "Газонная трава 2"
    assert grass2.description == "Выносливая трава"
    assert grass2.price == 450.0
    assert grass2.quantity == 15
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"
    assert grass2.color == "Темно-зеленый"


def test_smartphone_sum(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    """Тест на проверку суммирования стоимости товаров двух объектов Smartphone"""
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == 2580000.0


def test_grass_sum(grass1: LawnGrass, grass2: LawnGrass) -> None:
    """Тест на проверку суммирования стоимости товаров двух объектов LawnGrass"""
    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0


def test_invalid_sum(smartphone1: Smartphone, grass1: LawnGrass) -> None:
    """Тест на проверку суммирования стоимости двух объектов разных классов - Smartphone и LawnGrass"""
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_smartphone_to_category(smartphone1: Smartphone, smartphone2: Smartphone, smartphone3: Smartphone) -> None:
    """Тест на добавления товара смартфон в категорию смартфоны"""
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_smartphones.add_product(smartphone3)
    assert category_smartphones.products == (
        "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.\n"
    )

    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")  # type: ignore


def test_order_init(product1: Product) -> None:
    """Тест на цену и отображение информации о заказе для класса Order"""
    order = Order(product1, 2)
    assert order.total_price == 360000.0
    assert str(order) == "Заказ: Samsung Galaxy S23 Ultra, количество: 2, итоговая стоимость: 360000.0 руб."
