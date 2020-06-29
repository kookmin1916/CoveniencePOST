from model import Model
from product import ProductManager, Product
from log import LogManager, Log


class View:
    def __init__(self, model):
        self.model = model

    def show_products(self):
        print()
        product_list = self.model.product_manager.product_list
        for product in product_list:
            print(product.get_information())

    def show_chosen_products(self):
        print()
        product_list = self.model.chosen_list
        for product in product_list:
            print(product.get_information())

    def show_logs(self):
        print()
        log_list = self.model.log_manager.log_list
        for log in log_list:
            print(log.get_information())

    @staticmethod
    def show_main():
        print()
        print("1: 구매 관리, 2: 물건 관리, 3: 로그 관리, 4: 종료")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_purchase_controller():
        print()
        print("1: 구매, 2: 물건 선택, 3: 종료")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_add_product():
        print()
        print("구입할 물건의 id와 개수를 입력해 주세요: ")

    @staticmethod
    def show_lack():
        print()
        print("물건의 재고가 부족합니다.")

    @staticmethod
    def show_product_controller():
        print()
        print("1: 물건 목록 보기, 2: 물건 수정, 3: 물건 삭제, 4: 물건 추가, 5: 종료")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_log_controller():
        print()
        print("1: 로그 보기, 2: 로그 삭제, 3: 종료")
        print("숫자를 입력해 주세요: ")
