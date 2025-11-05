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

    @classmethod
    def new_product(
        cls, product_data: dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """
        Класс-метод создания продукта из словаря.
        """
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
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
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
            result += f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def product_list(self) -> List[Product]:
        return self.__products
