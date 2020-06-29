from product import ProductManager
from log import Log, LogManager


class PurchaseController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
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

        self.model.chosen_list = []
        self.view.show_finish_purchase()

        log_str = ""
        for i in range(len(self.model.chosen_list)):
            chosen_product = self.model.chosen_list[i]
            log_str += chosen_product[0].name + "-" + chosen_product[1]
            if i < len(self.model.chosen_list) - 1:
                log_str += ", "
        self.model.log_manager.add_log(Log(log_str))

    def add_product(self):
        self.view.show_products()

        self.view.show_string("구입할 물건의 id를 입력해 주세요: ")
        product_id = int(input())
        if product_id < 0 or product_id >= len(self.model.product_list):
            self.view.show_wrong_value()
            return

        self.view.show_string("구입할 물건의 개수를 입력해 주세요: ")
        number = int(input())

        if number <= 0:
            self.view.show_wrong_value()
            return

        if number > self.model.product_list[product_id].stock:
            self.view.show_lack_stock()
            return

        is_chosen = False
        for i in range(len(self.model.chosen_list)):
            chosen_product = self.model.chosen_list[i]
            if chosen_product[0] == product_id:
                is_chosen = True
                if number + chosen_product[1] > self.model.product_list[product_id].stock:
                    self.view.show_lack_stock()
                    return
                else:
                    chosen_product[1] += number
                break
        if not is_chosen:
            self.model.chosen_list += [[product_id, number]]

