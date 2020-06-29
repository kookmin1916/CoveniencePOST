from product import ProductManager, Product, GeneralProduct, FoodProduct, AgeRestrictedProduct


class ProductController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self.view.show_product_controller()
            number = int(input())
            if not 1 <= number <= 5:
                self.view.show_wrong_value()
                continue

            if number == 1:
                self.view.show_products()
            elif number == 2:
                self.add_product()
            elif number == 3:
                self.del_product()
            elif number == 4:
                self.revise_product()
            elif number == 5:
                break

    def add_product(self):
        self.view.show_products()

        product_number = self.input_product_id()
        if product_number == -1:
            return

        self.view.show_product_type()
        type_number = int(input())
        if not 1 <= type_number <= 3:
            self.view.show_wrong_value()
            return

        new_id = self.model.product_manager.get_new_id()
        if type_number == 1:
            self.view.show_string("이름, 가격, 설명, 재고를 입력해 주세요: ")
            name, price, explanation, stock = input().split(' ')
            self.model.product_manager.add_product(GeneralProduct(new_id, name, int(price), explanation, int(stock)))
        elif type_number == 2:
            self.view.show_string("이름, 가격, 설명, 재고, 유통기한을 입력해 주세요: ")
            name, price, explanation, stock, best_before = input().split(' ')
            self.model.product_manager.add_product(FoodProduct(
                new_id, name, int(price), explanation, int(stock), best_before))
        elif type_number == 3:
            self.view.show_string("이름, 가격, 설명, 재고, 제한연령을 입력해 주세요: ")
            name, price, explanation, stock, age_limit = input().split(' ')
            self.model.product_manager.add_product(AgeRestrictedProduct(
                new_id, name, int(price), explanation, int(stock), int(age_limit)))

        self.view.show_string("추가가 완료되었습니다.")

    def revise_product(self):
        self.view.show_products()

        product_number = self.input_product_id()
        if product_number == -1:
            return

        self.view.show_revise_type()
        type_number = int(input())
        if not 1 <= type_number <= 2:
            self.view.show_wrong_value()
            return

        product = self.model.product_manager.product_list[product_number]
        if type_number == 1:
            product.name = input()
        elif type_number == 2:
            product.stock = int(input())
        self.model.product_manager.devise_product(product_number, product)

        self.view.show_string("수정이 완료되었습니다.")

    def del_product(self):
        self.view.show_products()

        product_number = self.input_product_id()
        if product_number == -1:
            return

        self.model.product_manager.del_product(product_number)

        self.view.show_string("삭제가 완료되었습니다.")

    def input_product_id(self):
        self.view.show_string("물건의 id를 입력해 주세요")

        product_number = int(input())
        if product_number < 0 or product_number >= len(self.model.product_list):
            self.view.show_wrong_value()
            return -1
        return product_number
