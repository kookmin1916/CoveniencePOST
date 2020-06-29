from product import ProductManager, AgeRestrictedProduct
from log import Log, LogManager


class PurchaseController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self.view.show_chosen_products()
            self.view.show_purchase_controller()
            number = int(input())
            if not 1 <= number <= 3:
                self.view.show_wrong_value()
                continue

            if number == 1:
                self.buy()
            elif number == 2:
                self.add_product()
            elif number == 3:
                break

    def buy(self):
        if len(self.model.chosen_list) == 0:
            self.view.show_string("선택한 물건이 없습니다.")
            return

        max_age_limit = -1
        for chosen_product in self.model.chosen_list:
            product = self.model.product_manager.product_list[chosen_product[0]]
            if isinstance(product, AgeRestrictedProduct)\
                    and product.age_limit > max_age_limit:
                max_age_limit = product.age_limit

        if max_age_limit != -1:
            self.view.show_string("나이를 입력해 주세요: ")
            age = int(input())
            if age < max_age_limit:
                self.view.show_string("연령 제한에 저촉되는 상품이 있습니다.")
                return

        total_price = 0
        for chosen_product in self.model.chosen_list:
            product = self.model.product_manager.product_list[chosen_product[0]]
            total_price += product.price * chosen_product[1]

        self.view.show_total_price(total_price)
        money = int(input())
        if money < 0:
            self.view.show_wrong_value()
            return

        if money < total_price:
            self.view.show_string("금액이 부족합니다.")
            return

        for chosen_product in self.model.chosen_list:
            self.model.product_manager.product_list[chosen_product[0]].stock -= chosen_product[1]

        self.view.show_finish_purchase(money - total_price)

        log_str = ""
        for i in range(len(self.model.chosen_list)):
            chosen_product = self.model.chosen_list[i]
            log_str += self.model.product_manager.product_list[chosen_product[0]].name + "-" + str(chosen_product[1])
            if i < len(self.model.chosen_list) - 1:
                log_str += ", "
        self.model.log_manager.add_log(Log(log_str))

        self.model.chosen_list = []

    def add_product(self):
        self.view.show_products()

        self.view.show_string("구입할 물건의 id를 입력해 주세요: ")
        product_id = int(input())
        if product_id < 0 or product_id >= self.model.product_manager.product_list_size():
            self.view.show_wrong_value()
            return

        self.view.show_string("구입할 물건의 개수를 입력해 주세요: ")
        number = int(input())

        if number <= 0:
            self.view.show_wrong_value()
            return

        if number > self.model.product_manager.product_list[product_id].stock:
            self.view.show_lack_stock()
            return

        is_chosen = False
        for i in range(len(self.model.chosen_list)):
            chosen_product = self.model.chosen_list[i]
            if chosen_product[0] == product_id:
                is_chosen = True
                if number + chosen_product[1] > self.model.product_manager.product_list[product_id].stock:
                    self.view.show_lack_stock()
                    return
                else:
                    chosen_product[1] += number
                break
        if not is_chosen:
            self.model.chosen_list += [[product_id, number]]

