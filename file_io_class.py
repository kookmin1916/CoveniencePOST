from product import Product


def read_stuff_file():
    try:
        file = open("stuff_list.txt", 'r')
    except FileNotFoundError:
        open("stuff_list.txt", 'a').close()
        file = open("stuff_list.txt", 'r')
    stuff_list = []

    for line in file:
        name, price, explanation, stock = line[:-1].split("|")
        stuff_list += [Stuff(name, int(price), explanation, int(stock))]

    file.close()
    return stuff_list


def write_stuff_file(stuff_list):
    file = open("stuff_list.txt", 'w')
    for stuff in stuff_list:
        file.write(stuff.name + '|' + str(stuff.price) + '|' + stuff.explanation + '|' + str(stuff.stock) + '\n')
    file.close()


def read_log_file():
    try:
        file = open("log.txt", 'r')
    except FileNotFoundError:
        open("log.txt", 'a').close()
        file = open("log.txt", 'r')
    log_list = []

    for line in file:
        date, contents = line[:-1].split("|")
        log_list += ["날짜: %s, 내용: %s" % (date, contents)]

    file.close()
    return log_list


def add_log_file(new_log):
    file = open("log.txt", 'a')
    file.write(new_log + '\n')


if __name__ == "__main__":
    a = read_stuff_file()
    print(a[0], a[1])
    write_stuff_file(a)
