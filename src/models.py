from typing import List


class Product:
    """Класс представляющий продукты"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """
        Класс-метод создания продукта из словаря.
        """
        new_name = product_data.get("name")
        new_description = product_data.get("description")
        new_price = product_data.get("price")
        new_quantity = product_data.get("quantity")

        if existing_products is not None:
            for prod in existing_products:
                if prod.name == new_name:
                    prod.quantity += new_quantity
                    if new_price > prod.price:
                        prod.price = new_price
                    return prod
        return cls(new_name, new_description, new_price, new_quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс представляющий категории товаров"""

    name: str
    description: str
    __products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
