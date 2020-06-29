class ProductManager:
    def __init__(self):
        self.__product_list = self.__read_file()

    def add_product(self, product):
        self.__product_list += [product]

    def del_product(self, product_id):
        del self.__product_list[product_id]
        for i in range(len(self.__product_list)):
            self.__product_list[i].id = i

    def devise_product(self, product_id, product):
        self.__product_list[product_id] = product

    def get_new_id(self):
        return len(self.__product_list)

    @staticmethod
    def __read_file():
        product_list = []
        try:
            file = open("product_list.txt", 'r')
        except FileNotFoundError:
            open("product_list.txt", 'a').close()
            file = open("product_list.txt", 'r')

        product_id = 0
        for line in file:
            information = line[:-1].split("|")
            if information[0] == "GeneralProduct":
                product_list += [GeneralProduct(product_id, information[1], information[2], information[3], information[4])]
            elif information[0] == "FoodProduct":
                product_list += [FoodProduct(product_id, information[1], information[2],
                                             information[3], information[4], information[5])]
            elif information[0] == "AgeRestrictedProduct":
                product_list += [AgeRestrictedProduct(product_id, information[1], information[2],
                                                      information[3], information[4], information[5])]
            else:
                raise
            product_id += 1

        file.close()
        return product_list

    @staticmethod
    def __write_file(product_list):
        file = open("product_list.txt", 'w')
        for product in product_list:
            file.write(product.get_file_information())
        file.close()

    @property
    def product_list(self):
        return self.__product_list

    def __del__(self):
        self.__write_file(self.__product_list)


class Product:
    def __init__(self, product_id, name, price, explanation, stock):
        self.__id = product_id
        self.__name = name
        self.__price = price
        self.__explanation = explanation
        self.__stock = stock
        self.__type = "Product"

    def __str__(self):
        return "{" + self.get_information() + "}"

    def get_information(self):
        return "id: %d, name: %s, price: %d, explanation: %s, stock: %d"\
               % (self.__id, self.__name, self.__price, self.__explanation, self.__stock)

    def get_file_information(self):
        return self.__type + "|" + self.__name + "|" + self.__price + "|" + self.__explanation + "|" + self.__stock

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

    @property
    def type(self):
        return self.__type

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, product_id):
        self.__id = product_id


class GeneralProduct(Product):
    def __init__(self, product_id, name, price, explanation, stock):
        super().__init__(product_id, name, price, explanation, stock)
        self.__type = "GeneralProduct"


class FoodProduct(Product):
    def __init__(self, product_id, name, price, explanation, stock, best_before):
        super().__init__(product_id, name, price, explanation, stock)
        self.__best_before = best_before
        self.__type = "FoodProduct"

    def get_information(self):
        return super().get_information() + ", best before: %s" % self.__best_before

    def get_file_information(self):
        return super().get_file_information() + "|" + self.__best_before

    @property
    def best_before(self):
        return self.__best_before


class AgeRestrictedProduct(Product):
    def __init__(self, product_id, name, price, explanation, stock, age_limit):
        super().__init__(product_id, name, price, explanation, stock)
        self.__age_limit = age_limit
        self.__type = "AgeRestrictedProduct"

    def get_information(self):
        return super().get_information() + ", age limit: %d" % self.__age_limit

    def get_file_information(self):
        return super().get_file_information() + "|" + self.__age_limit

    @property
    def age_limit(self):
        return self.__age_limit
