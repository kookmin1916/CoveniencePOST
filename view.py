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
        chosen_list = self.model.chosen_list
        for chosen_product in chosen_list:
            print(chosen_product[0].name + ": " + chosen_product[1])

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
    def show_total_price(total_price):
        print()
        print("총액: " + str(total_price))
        print("받은 금액을 입력해 주세요: ")

    @staticmethod
    def show_finish_purchase(change):
        print()
        print("결제가 완료되었습니다.")
        print("거스름돈: " + str(change))

    @staticmethod
    def show_lack_stock():
        print()
        print("물건의 재고가 부족합니다.")

    @staticmethod
    def show_product_controller():
        print()
        print("1: 물건 목록 보기, 2: 물건 추가, 3: 물건 삭제, 4: 물건 수정, 5: 종료")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_product_type():
        print()
        print("1: 일반 상품, 2: 음식물, 3: 연령제한 물품")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_revise_type():
        print()
        print("1: 가격 수정, 2: 재고 수정")
        print("숫자를 입력해 주세요: ")
        
    @staticmethod
    def show_log_controller():
        print()
        print("1: 로그 보기, 2: 로그 전체 삭제, 3: 종료")
        print("숫자를 입력해 주세요: ")

    @staticmethod
    def show_wrong_value():
        print()
        print("옳바른 값을 입력해 주세요.")

    @staticmethod
    def show_string(string):
        print()
        print(string)
