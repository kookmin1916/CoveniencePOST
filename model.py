from product import ProductManager, Product
from log import LogManager


class Model:
    def __init__(self):
        self.product_manager = ProductManager()
        self.chosen_list = []
        self.log_manager = LogManager()
