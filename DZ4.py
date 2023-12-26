"""
1. Напишите функцию для транспонирования матрицы
"""
def matrix_t_zip(matrix: list) -> list:
    ''' На вход ожидается матрица формата:
    [[a,b,c],
    [d,e,f],
    [g,k,l]]'''
    return list(map(list,zip(*matrix)))

def matrix_t(matrix: list) -> list:
    new_matrix = []
    for j in range(len(matrix[0])):
        line = []
        for i in range(len(matrix)):
            line.append(matrix[i][j])
        new_matrix.append(line.copy())
    return new_matrix

array = [[1,2],[3,4],[5,6]]

print(matrix_t_zip(array))
print(matrix_t(array))


"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""
def dict_(**kwargs):
    newdict = {}
    for key, value in kwargs.items():
        newdict[str(value)] = key
    return newdict

print(dict_(Moscow = 77, SanctPeterburg = 78, Tula = 71))

"""
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from datetime import datetime

MIN_DELTA = 50
ITER = 3
PERS = 1.03
COMMISSION_PERSENT = 1.5
COMMISSION_MIN = 30
COMMISSION_MAX = 600
MAX_BALANCE = 5_000_000
log = []

def check_tax(balance):
    if balance > MAX_BALANCE:
        balance *= 0.9
    return balance

def add_percent(balance):
   return balance * PERS

def get_percent(delta):
    temp = delta * COMMISSION_PERSENT / 100
    if temp < COMMISSION_MIN:
        temp = COMMISSION_MIN
    elif temp > COMMISSION_MAX:
        temp = COMMISSION_MAX
    return temp


def add(balance, count_iter):
    while True:
        delta = input("Введите сумму пополнения: ")
        if delta.isdigit():
            delta = int(delta)
            if delta % MIN_DELTA != 0:
                print(f"Введите сумму кратную {MIN_DELTA}")
            else:
                break
        else:
            print("Введите число")
    balance += delta
    count_iter += 1
    if count_iter % ITER == 0:
        balance = add_percent(balance)
    add_log(f"Пополнение: {delta}, текущий баланс: {balance}")
    return balance, count_iter

def get(balance, count_iter):
    while True:
        delta = input("Введите сумму снятия: ")
        if delta.isdigit():
            delta = int(delta)
            if delta % MIN_DELTA != 0:
                print(f"Введите сумму кратную {MIN_DELTA}")
            else:
                temp = get_percent(delta)
                if temp + delta > balance:
                    print(f"У вас недостаточно денег")
                else:
                    break
        else:
            print("Введите число")
    balance -= delta + temp
    count_iter += 1
    if count_iter % ITER != 0:
        balance = add_percent(balance)
    add_log(f"Снятие: -{delta}, текущий баланс: {balance}")
    return balance, count_iter

def print_sum(a):
    print(f"На вашем счету {a} у.е.")

def menu():
    menu_text = """
    1. Пополнить
    2. Снять
    3. Список операций
    4. Выйти
    """
    user_input = ""
    balance = 0
    count_iter = 0
    while True:
        print(menu_text)
        while True:
            user_input = input("Введите номер пункта: ")
            if user_input in ("1", "2", "3"):
                break
        if user_input == "1":
            balance = check_tax(balance)
            balance, count_iter = add(balance,count_iter)
            print_sum(balance)
        elif user_input == "2":
            balance = check_tax(balance)
            balance, count_iter = get(balance,count_iter)
            print_sum(balance)
        elif user_input == "3":
            get_log()
        elif user_input == "4":
            print_sum(balance)
            break

def add_log(event):
    global log
    log.append(datetime.now().strftime('%Y.%m.%d %H:%M:%S') + " - " + event)
    return log[-1]

def get_log():
    global log
    print("Список операций:")
    if len(log):
        for num, el in enumerate(log):
            print(str(num + 1) + ". " + el)
    else:
        print("Список пуст...")

if __name__ == "__main__":
    menu()
