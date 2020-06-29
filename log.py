import time


class LogManager:
    def __init__(self):
        self.__log_list = self.__read_file()
        self.__file = open("log.txt", 'a')

    def add_log(self, new_log):
        self.__log_list += [new_log]
        self.__file.write(new_log + '\n')

    @staticmethod
    def __read_file():
        log_list = []
        try:
            file = open("log.txt", 'r')
        except FileNotFoundError:
            open("log.txt", 'a').close()
            file = open("log.txt", 'r')

        for line in file:
            date, content = line[:-1].split("|")
            log_list += [Log(content, date)]

        file.close()
        return log_list

    @staticmethod
    def __write_file(log_list):
        file = open("log.txt", 'w')
        for log in log_list:
            file.write(log.get_file_information())
        file.close()

    @property
    def log_list(self):
        return self.__log_list


class Log:
    def __init__(self, content, date=None):
        if date is None:
            self.__date = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
        else:
            self.__date = date
        self.__content = content

    def __str__(self):
        return "{" + self.get_information() + "}"

    def get_information(self):
        return "date: {}, content: {}".format(self.__date, self.__content)

    def get_file_information(self):
        return "{}|{}".format(self.__date, self.__content)

    @property
    def date(self):
        return self.__date

    @property
    def content(self):
        return self.__content
