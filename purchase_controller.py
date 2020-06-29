from product import ProductManager


class PurchaseController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self.view.show_purchase_controller()
            number = input()

            if number == '1':
                self.buy()
            elif number == '2':
                self.add_product()
            elif number == '3':
                break

    def buy(self):
        total_price = 0
        log = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time())) + "|"
        for idx in range(len(self.chosen_list)):
            chosen_product = self.chosen_list[idx]
            total_price += chosen_product[1] * self.product_list[chosen_product[0]].price
            log += self.product_list[chosen_product[0]].name + "-" + str(chosen_product[1])
            if idx != len(self.chosen_list) - 1:
                log += ", "

        money = int(input())
        if money < 0:
            raise ValueError

        if money < total_price:
            print("금액이 부족합니다.")
            continue

        for idx in range(len(self.chosen_list)):
            chosen_product = self.chosen_list[idx]
            self.product_list[chosen_product[0]].stock -= chosen_product[1]

        write_product_file(self.product_list)
        add_log_file(log)
        self.chosen_list = []

        print("결제가 완료되었습니다.")
        print("거스름돈: " + str(money - total_price))

    def add_product(self):
        self.show_product_list()

        print("구입할 물건의 번호를 입력해 주세요: ")
        product_number = int(input())
        if product_number < 0 or product_number >= len(self.product_list):
            raise ValueError

        print("구입할 개수를 입력해 주세요: ")
        count = int(input())
        if count > self.product_list[product_number].stock:
            print("물건의 재고가 부족합니다.")
            continue
        if count <= 0:
            raise ValueError

        is_chosen = False
        for idx in range(len(self.chosen_list)):
            if self.chosen_list[idx][0] == product_number:
                is_chosen = True
                if count + self.chosen_list[idx][1] > self.product_list[product_number].stock:
                    print("물건의 재고가 부족합니다.")
                else:
                    self.chosen_list[idx][1] += count
                break
        if not is_chosen:
            self.chosen_list += [[product_number, count]]

