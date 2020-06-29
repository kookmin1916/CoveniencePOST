from product import ProductManager


class PurchaseController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self.view.show_purchase_controller()

