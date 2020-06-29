from purchase_controller import PurchaseController
from product_controller import ProductController
from log_controller import LogController


class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model

        self.__purchase_controller = PurchaseController(model=model, view=view)
        self.__product_controller = ProductController(model=model, view=view)
        self.__log_controller = LogController(model=model, view=view)

    def run(self):
        while True:
            self.view.show_main()
            number = int(input())
            if not 1 <= number <= 4:
                self.view.show_wrong_value()
                continue

            if number == 1:
                self.__purchase_controller.run()
            elif number == 2:
                self.__product_controller.run()
            elif number == 3:
                self.__log_controller.run()
            elif number == 4:
                break
