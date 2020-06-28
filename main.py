from file_io import add_log_file, read_log_file, write_product_file, read_product_file
import time
from product import Product


class Main:
    def __init__(self):
        self.product_list = read_product_file()
        self.chosen_list = []

    def run(self):
        while True:
            print()
            print("1: 구매 관리, 2: 물건 관리, 3: 로그 보기, 4: 종료")
            print("숫자를 입력해 주세요: ")
            number = input()

            if number == '1':
                self.buy()
            elif number == '2':
                self.manage_product()
            elif number == '3':
                self.show_log()
            elif number == '4':
                break
            else:
                print("올바른 숫자를 입력해 주세요.")

    def buy(self):
        while True:
            try:
                print()
                if len(self.chosen_list) != 0:
                    print("#선택한 물건")
                    for chosen_product in self.chosen_list:
                        print("이름: %s, 개수: %d" % (self.product_list[chosen_product[0]].name, chosen_product[1]))

                print("1: 구매, 2: 물건 선택, 3: 종료")
                print("숫자를 입력해 주세요: ")
                number = input()

                if number == '1':
                    total_price = 0
                    log = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time())) + "|"
                    for idx in range(len(self.chosen_list)):
                        chosen_product = self.chosen_list[idx]
                        total_price += chosen_product[1] * self.product_list[chosen_product[0]].price
                        log += self.product_list[chosen_product[0]].name + "-" + str(chosen_product[1])
                        if idx != len(self.chosen_list) - 1:
                            log += ", "

                    print("총액: " + str(total_price))
                    print("받은 금액을 입력해 주세요: ")
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

                elif number == '2':
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

                elif number == '3':
                    break

                else:
                    print("올바른 숫자를 입력해 주세요.")

            except ValueError:
                print("올바른 값을 입력해 주세요.")
                continue
        self.chosen_list = []

    def manage_product(self):
        while True:
            try:
                print()
                print("1: 물건 목록 보기, 2: 물건 수정, 3: 물건 삭제, 4: 물건 추가, 5: 종료")
                print("숫자를 입력해 주세요: ")
                number = input()
                if number == '1':
                    self.show_product_list()

                elif number == '2':
                    self.show_product_list()
                    print("정보를 수정할 물건의 번호를 입력해 주세요: ")
                    product_number = int(input())
                    if product_number < 0 or product_number >= len(self.product_list):
                        raise ValueError

                    print("이름, 가격, 설명, 재고를 입력해 주세요: ")
                    name, price, explanation, stock = input().split(' ')
                    self.product_list[product_number] = Stuff(name, int(price), explanation, int(stock))

                    write_product_file(self.product_list)
                    print("수정이 완료되었습니다.")

                elif number == '3':
                    self.show_product_list()
                    print("삭제할 물건의 번호를 입력해 주세요: ")
                    product_number = int(input())
                    if product_number < 0 or product_number >= len(self.product_list):
                        raise ValueError

                    new_product_list = []
                    for idx in range(len(self.product_list)):
                        if idx != product_number:
                            new_product_list += [self.product_list[idx]]

                    self.product_list = new_product_list
                    write_product_file(self.product_list)
                    print("삭제가 완료되었습니다.")

                elif number == '4':
                    print("이름, 가격, 설명, 재고를 입력해 주세요: ")
                    name, price, explanation, stock = input().split(' ')
                    self.product_list += [Stuff(name, int(price), explanation, int(stock))]

                    write_product_file(self.product_list)
                    print("추가가 완료되었습니다.")

                elif number == '5':
                    break

                else:
                    print("올바른 숫자를 입력해 주세요.")

            except ValueError:
                print("올바른 값을 입력해 주세요.")
                continue

    def show_log(self):
        log = read_log_file()
        for i in log:
            print(i)

    def show_product_list(self):
        print("#물건 리스트")
        for idx in range(len(self.product_list)):
            product = self.product_list[idx]
            print("번호: %d, 이름: %s, 가격: %d, 설명: %s, 재고: %d" % (
                  idx, product.name, product.price, product.explanation, product.stock))


if __name__ == "__main__":
    controller = Main()
    controller.run()
