from typing import Any, List, Optional


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

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Product,
        включающее имя, цену и количество в наличии"""
        return f"{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        """Суммирует стоимость товаров двух объектов Product"""
        if isinstance(other, type(self)):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(
        cls, product_data: dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """Класс-метод создания продукта из словаря"""
        new_name = product_data.get("name")
        new_description = product_data.get("description")
        new_price = product_data.get("price")
        new_quantity = product_data.get("quantity")

        if not isinstance(new_name, str):
            raise ValueError("Product name must be a string")
        if not isinstance(new_description, str):
            new_description = ""
        if not isinstance(new_price, (int, float)):
            raise ValueError("Product price must be a number")
        if not isinstance(new_quantity, int):
            raise ValueError("Product quantity must be an integer")

        if existing_products is not None:
            for prod in existing_products:
                if prod.name == new_name:
                    prod.quantity += new_quantity
                    if new_price > prod.price:
                        prod.price = new_price
                    return prod
        return cls(new_name, new_description, new_price, new_quantity)

    @property
    def price(self) -> float:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает цену товара"""
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    """Класс представляющий товар - смартфоны"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс представляющий товар - трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        Category.product_count += sum(p.quantity for p in products)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Category,
        включающее имя и общее количество"""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity}"

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += product.quantity
        else:
            raise TypeError("Добавлять можно только объекты класса Product или его наследников")

    @property
    def products(self) -> str:
        """Возвращает строку со списком всех продуктов категории"""
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    @property
    def product_list(self) -> List[Product]:
        """Возвращает список объектов Product в категории."""
        return self.__products

    def __iter__(self) -> "ProductIterator":
        return ProductIterator(self)


class ProductIterator:
    """Итератор по списку продуктов категории"""

    def __init__(self, category_obj: Any) -> None:
        """Инициализирует итератор"""
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Возвращает себя как итератор."""
        return self

    def __next__(self) -> Any:
        """Возвращает следующий продукт категории"""
        if self.index < len(self.category.product_list):
            products = self.category.product_list[self.index]
            self.index += 1
            return products

        else:
            raise StopIteration


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)