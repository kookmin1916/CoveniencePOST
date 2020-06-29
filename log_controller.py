from log import LogManager


class LogController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self.view.show_log_controller()
            number = int(input())
            if not 1 <= number <= 3:
                self.view.show_wrong_value()
                continue

            if number == 1:
                self.view.show_logs()
            elif number == 2:
                self.del_log()
            elif number == 3:
                break

    def del_log(self):
        self.model.view.show_string("정말 삭제하시겠습니까?(y/n): ")
        check = input()
        if check == 'y':
            self.model.log_manager.del_log()
