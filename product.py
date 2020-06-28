from abc import abstractmethod


class ProductController:
    def __init__(self):
        self.__product_list = self.__read_file()

    def add_product(self, product):
        self.__product_list += [product]

    @staticmethod
    def __read_file():
        product_list = []
        try:
            file = open("product_list.txt", 'r')
        except FileNotFoundError:
            open("product_list.txt", 'a').close()
            file = open("product_list.txt", 'r')

        for line in file:
            name, price, explanation, stock = line[:-1].split("|")
            product_list += [Product(name, int(price), explanation, int(stock))]

        file.close()
        return product_list

    @staticmethod
    def __write_file(product_list):
        file = open("product_list.txt", 'w')
        for product in product_list:
            file.write(product.name + '|' + str(product.price) + '|'
                       + product.explanation + '|' + str(product.stock) + '\n')
        file.close()

    def __del__(self):
        self.__write_file(self.__product_list)


class Product:
    def __init__(self, name, price, explanation, stock):
        self.__name = name
        self.__price = price
        self.__explanation = explanation
        self.__stock = stock

    def __str__(self):
        return "{name: %s, price: %d, explanation: %s, stock: %d}"\
               % (self.__name, self.__price, self.__explanation, self.__stock)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise
        self.__price = price

    @property
    def explanation(self):
        return self.__explanation

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            raise
        self.__stock = stock


class GeneralProduct(Product):
    def __init__(self, name, price, explanation, stock):
        super().__init__(name, price, explanation, stock)


class FoodProduct(Product):
    def __init__(self, name, price, explanation, stock, best_before):
        super().__init__(name, price, explanation, stock)
        self.__best_before = best_before

    @property
    def best_before(self):
        return self.__best_before
