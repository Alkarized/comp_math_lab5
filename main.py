# # Вариант 13 - Многочлен Лагранжа и Многочлен Гаусса
# import sympy
# from tabulate import tabulate
# import math
# import matplotlib.pyplot as plt
# import numpy as np
# from sympy import Symbol
#
#
# class Function:
#     def __init__(self, equation, text):
#         self.equation = equation
#         self.text = text
#
#
# class Method:
#     def __init__(self, func, text):
#         self.func = func
#         self.text = text
#
#
# isNotPrinted = True
#
#
# def graph(x_list, y_list, metds, x0, results):
#     plt.figure()
#     # plt.grid(True)
#     plt.title = "Графики"
#     plt.scatter(x_list, y_list, s=20, label='Исходные данные', zorder=10)
#     x_linspace = np.linspace(x_list[0], x_list[-1], 100)
#
#     i = 0
#     for method in metds:
#         interpolated_y = []
#         for x in x_linspace:
#             mi, msg = method.func(x_list, y_list, x)
#             interpolated_y.append(mi)
#         plt.plot(x_linspace, interpolated_y, zorder=5, label=method.text)
#         plt.plot(x0, results[i], 'X', markersize=5, zorder=10, label=method.text)
#         i += 1
#
#     plt.legend(fontsize='x-small')
#     plt.show()
#
#
# def coef_lagr(x_list, x0, yi, i):
#     ans = yi
#     for j in range(len(x_list)):
#         if j == i:
#             continue
#         ans *= (x0 - x_list[j])
#         ans /= (x_list[i] - x_list[j])
#     return ans
#
#
# def check_diff(x_list):
#     dif = x_list[0] - x_list[1]
#     for i in range(1, len(x_list) - 1):
#         if not math.isclose(x_list[i] - x_list[i + 1], dif):
#             return False
#     return True
#
#
# def lagrange(x_list, y_list, x0):
#     sum_t = 0
#     for i in range(len(x_list)):
#         sum_t += coef_lagr(x_list, x0, y_list[i], i)
#     sum_t = sum_t
#     return sum_t, ""
#
#
# def diff_table(x_list, y_list):
#     datatable = list()
#     for i in range(len(y_list)):
#         datatable.append([x_list[i], y_list[i]])
#
#     for i in range(len(y_list) - 1):
#         for j in range(len(y_list) - i - 1):
#             datatable[i].append(0)
#
#     for i in range(len(y_list) - 1):
#         for j in range(len(y_list) - 1 - i):
#             datatable[j][2 + i] = datatable[j + 1][1 + i] - datatable[j][1 + i]
#
#     return datatable
#
#
# def gauss(x_list, y_list, x0):  # i use first Gauss method!
#     ans = 0
#     msg = ""
#
#     if not check_diff(x_list):
#         print("Введенные данные неккоректны, узлы не равностоящие!")
#         return None
#     isLeft = None
#     middle = int(len(x_list) // 2)
#     if len(x_list) % 2 == 0:
#         middle -= 1
#     if x_list[middle] > x0:
#         isLeft = False  # second x - x0
#     else:
#         isLeft = True  # first x0 - x
#
#     datatable = diff_table(x_list, y_list)
#
#     header = ["xi", "yi"]
#     [header.append(f"d{i + 1} yi") for i in range(len(y_list) - 1)]
#
#     global isNotPrinted
#     if isNotPrinted:
#         print("Таблица конечных разностей:")
#         print(tabulate(datatable, header, tablefmt="grid", floatfmt="7.3f"))
#         isNotPrinted = False
#
#     step = x_list[1] - x_list[0]
#
#     ans = datatable[middle][1]
#
#     if isLeft:
#         t = (x0 - x_list[middle]) / step
#         key_t = t
#         ans += key_t * datatable[middle][2]
#         for i in range(1, middle * 2):
#             if i % 2 == 0:
#                 key_t += (t + i) / i
#                 ans += key_t * datatable[middle - i // 2][2 + i]
#             else:
#                 key_t += (t - i) / i
#                 ans += key_t * datatable[middle - i // 2 - 1][2 + i]
#
#     else:
#         t = (x_list[middle] - x0) / step
#
#         key_t = t * datatable[middle - 1][2]
#         for i in range(1, middle * 2):
#             if i % 2 == 1:
#                 key_t += (t + i) / i
#                 ans += key_t * datatable[middle - (i + 1) // 2][2 + i]
#             else:
#                 key_t += (t - i) / i
#                 ans += key_t * datatable[middle - i // 2 - 1][2 + i]
#
#     # ans = y_list[found_i] + t * datatabl  e[found_i - 1][2] + t * (t - 1) / 2 * datatable[found_i - 1][3]
#     return ans, msg
#
#
# x = Symbol("x")
# mn_min = -100
# mx_max = 100
# N_MIN = 2
# N_MAX = 20
#
# functions = list()
# functions.append(Function(x ** 3 + 2 * x ** 2 - 5 * x - 6, "x^3 + 2x^2 - 5x - 6"))
# functions.append(Function(sympy.sin(x), "sin(x)"))
# functions.append(Function(x ** 2, "x^2"))
#
# methods = list()
# methods.append(Method(lagrange, "Многочлен Лагранжа"))
# methods.append(Method(gauss, "Многочлен Гаусса"))
#
#
# def read_interval():
#     while True:
#         left = read_float(f"Введите левую границу из интервала ({mn_min};{mx_max}): ", mn_min, mx_max,
#                           "Введено неправильное значение левой границы!")
#         right = read_float(f"Введите левую границу из интервала ({left};{mx_max}): ", mn_min, mx_max,
#                            "Введено неправильное значение правой границы!")
#         if left >= right:
#             print("Левая граница больше или равна правой, ошибочка, давай по новой, все фигня")
#             continue
#         else:
#             return left, right
#
#
# def read_int(text, mn, mx, error_msg):
#     while True:
#         try:
#             val = int(input(text))
#             if mn <= val <= mx:
#                 return val
#             else:
#                 raise ValueError
#         except ValueError:
#             print(error_msg)
#
#
# def read_float(text, mn, mx, error_msg) -> float:
#     while True:
#         try:
#             val = float(input(text))
#             if mn < val < mx:
#                 return val
#             else:
#                 raise ValueError
#         except ValueError:
#             print(error_msg)
#
#
# def read_two_numbers():
#     text_in = input()
#     if text_in == "":
#         return None, None
#     else:
#         text_in = text_in.split()
#         if len(text_in) == 2:
#             return float(text_in[0]), float(text_in[1])
#         else:
#             raise ValueError
#
#
# def read_table():
#     print("Введите данные формата \"X Y\" в строчку, для окончания перечисления достаточно напечатать пустую строчку,"
#           " без пробелов.")
#     xx_list = list()
#     yy_list = list()
#     while True:
#         try:
#             xx, yy = read_two_numbers()
#             if xx is None and yy is None:
#                 if len(xx_list) < N_MIN:
#                     print("Куда пошел, ану сделай по чебуречески все, введи еще данные!!!!! Только " + str(
#                         len(xx_list)) + " ввел")
#                 else:
#                     break
#             else:
#                 if xx_list.count(xx):
#                     print(f"Такой x = {'{:.3f}'.format(xx)} уже есть, иди в пень! ")
#                 else:
#                     xx_list.append(xx)
#                     yy_list.append(yy)
#         except ValueError:
#             print("Введен неверный формат данных, попробуйте еще раз.")
#     return xx_list, yy_list
#
#
# def main():
#     type_index = read_int("Выберите ввод данных: \n1. Готовая функция.\n2. Таблица данных.\n", 1, 2,
#                           "Неправильный выбор, еще раз!")
#     if type_index == 1:
#         func_index = read_int(
#             "Выберите функцию: \n" + "\n".join([f'{i + 1}. {functions[i].text}' for i in range(len(functions))]) + "\n",
#             1, len(functions), "Неправильный выбор, еще раз!") - 1
#         left, right = read_interval()
#         amount = read_int(f"Введите кол-во узлов интерполяции [{N_MIN};{N_MAX}]: ", N_MIN, N_MAX,
#                           "Ошибка ввода кол-ва узлов!")
#         x_list = np.linspace(left, right, amount)
#         y_list = list()
#         for temp in x_list:
#             y_list.append(functions[func_index].equation.subs(x, temp))
#     else:
#         x_list, y_list = read_table()
#         x_list, y_list = zip(*sorted(zip(x_list, y_list)))
#         left = x_list[0]
#         right = x_list[-1]
#         amount = len(x_list)
#
#     x0 = read_float(f'Введите аргумент x0 ({"{:.3f}".format(left)};{"{:.3f}".format(right)}): ', left, right,
#                     "Введен крингэ")
#
#     print("\nИсходная таблица:\n" + tabulate([x_list, y_list], tablefmt='grid', floatfmt='7.3f') + "\n")
#
#     allowed_meths = []
#     results = []
#
#     for method in methods:
#         ans, msg = method.func(x_list, y_list, x0)
#         if ans is None:
#             print(method.text + ":", msg)
#         else:
#             allowed_meths.append(method)
#             results.append(ans)
#             print(method.text + ":", '{:.3f}'.format(ans))
#     graph(x_list, y_list, allowed_meths, x0, results)
#
#
# if "__main__" == __name__:
#     main()


# Вариант 13 - Многочлен Лагранжа и Многочлен Гаусса
import sympy
from tabulate import tabulate
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol


class Function:
    def __init__(self, equation, text):
        self.equation = equation
        self.text = text


class Method:
    def __init__(self, func, text):
        self.func = func
        self.text = text


isNotPrinted = True


def graph(x_list, y_list, metds, x0, results):
    plt.figure()
    # plt.grid(True)

    plt.title = "Графики"
    plt.scatter(x_list, y_list, s=20, label='Исходные данные', zorder=10)
    x_linspace = np.linspace(x_list[0], x_list[-1], 100)

    i = 0
    for method in metds:
        # if method.func == gauss:
        #     found = -1
        #     for i in range(1, len(x_list) - 1):
        #         if x_list[i] <= x0 <= x_list[i + 1]:
        #             found = i
        #             break
        #     x_linspace = np.linspace(x_list[found - 1], x_list[found + 1], 20)
        interpolated_y = []
        x_linspace_this = []
        for xx in x_linspace:
            mi, msg = method.func(x_list, y_list, xx)
            if mi is not None:
                x_linspace_this.append(xx)
                interpolated_y.append(mi)
        plt.plot(x_linspace_this, interpolated_y, zorder=5, label=method.text)
        plt.plot(x0, results[i], 'X', markersize=5, zorder=10, label=method.text)
        i += 1

    plt.legend(fontsize='x-small')
    plt.show()


def coef_lagr(x_list, x0, yi, i):
    ans = yi
    for j in range(len(x_list)):
        if j == i:
            continue
        ans *= (x0 - x_list[j])
        ans /= (x_list[i] - x_list[j])
    return ans


def check_diff(x_list):
    dif = x_list[0] - x_list[1]
    for i in range(1, len(x_list) - 1):
        if not math.isclose(x_list[i] - x_list[i + 1], dif):
            return False
    return True


def lagrange(x_list, y_list, x0):
    sum_t = 0
    for i in range(len(x_list)):
        sum_t += coef_lagr(x_list, x0, y_list[i], i)
    sum_t = sum_t
    return sum_t, ""


def diff_table(x_list, y_list): #, i_start, i_end):
    datatable = list()
    for i in range(len(y_list)):
    # for i in range(i_start, i_end):
        datatable.append([x_list[i], y_list[i]])

    for i in range(len(y_list) - 1):
    # for i in range(i_end - i_start - 1):
        for j in range(len(y_list) - i - 1):
        # for j in range(i_end - i_start - i - 1):
            datatable[i].append(0)

    for i in range(len(y_list) - 1):
    # for i in range(i_end - i_start - 1):
        for j in range(len(y_list) - 1 - i):
        # for j in range(i_end - i_start - i - 1):
            datatable[j][2 + i] = datatable[j + 1][1 + i] - datatable[j][1 + i]

    return datatable


def gauss2(x_list, y_list, x0):  # i use first Gauss method!
    ans = 0
    msg = ""

    if not check_diff(x_list):
        print("Введенные данные неккоректны, узлы не равностоящие!")
        return None
    found_i = -1
    for i in range(1, len(x_list) - 1):
        if x_list[i] <= x0 <= x_list[i + 1]:
            found_i = i
            break
    if found_i == -1:
        msg = "Ошибка поиска нужного элемента, ввели фигню, так что сами и страдайте!"
        return None, msg
    # if found_i > len(x_list) // 2:
    #     i_start = len(x_list) - 2 * found_i
    #     i_end = len(x_list)
    # else:
    #     i_start = 0
    #     i_end = found_i * 2 + 1
    datatable = diff_table(x_list, y_list, )# i_start, i_end)

    header = ["xi", "yi"]
    [header.append(f"d{i + 1} yi") for i in range(len(y_list) - 1)]

    global isNotPrinted
    if isNotPrinted:
        print("Таблица конечных разностей:")
        print(tabulate(datatable, header, tablefmt="grid", floatfmt="7.3f"))
        isNotPrinted = False

    step = x_list[1] - x_list[0]

    found_i = (len(x_list) - 1)// 2

    t = (x0 - x_list[found_i]) / step

    # ans = y_list[found_i] + t * datatable[found_i - 1][2] + t * (t - 1) / 2 * datatable[found_i - 1][3]
    ans = y_list[found_i]
    temp = 1
    for i in range(1, 2*found_i + 1):
        temp /= i
        if i % 2 == 0:
            temp *= (t + i // 2)
        else:
            temp *= (t - i // 2)
        ans += temp * datatable[found_i - (i + 1) // 2][i + 1]
        print(datatable[found_i - (i + 1) // 2][i + 1])
    return ans, msg


def gauss(x_list, y_list, x0):  # i use first Gauss method!
    ans = 0
    msg = ""

    if not check_diff(x_list):
        print("Введенные данные неккоректны, узлы не равностоящие!")
        return None
    found_i = -1
    for i in range(1, len(x_list) - 1):
        if x_list[i] <= x0 <= x_list[i + 1]:
            found_i = i
            break
    if found_i == -1:
        msg = "Ошибка поиска нужного элемента, ввели фигню, так что сами и страдайте!"
        return None, msg

    # if found_i > len(x_list) // 2:
    #     i_start = len(x_list) - 2 * found_i - 1
    #     i_end = len(x_list)
    # else:
    #     i_start = 0
    #     i_end = found_i * 2 + 1
    datatable = diff_table(x_list, y_list ) #, i_start, i_end)

    header = ["xi", "yi"]
    [header.append(f"d{i + 1} yi") for i in range(len(y_list) - 1)]

    global isNotPrinted
    if isNotPrinted:
        print("Таблица конечных разностей:")
        print(tabulate(datatable, header, tablefmt="grid", floatfmt="7.3f"))
        isNotPrinted = False
        print(datatable)

    step = x_list[1] - x_list[0]

    found_i = (len(x_list) - 1) // 2

    t = (x0 - x_list[found_i]) / step

    # ans = y_list[found_i] + t * datatable[found_i - 1][2] + t * (t - 1) / 2 * datatable[found_i - 1][3]
    ans = y_list[found_i]
    temp = 1
    for i in range(1, 2*found_i + 1):
        temp /= i
        if i % 2 == 0:
            temp *= (t - i // 2)
        else:
            temp *= (t + i // 2)
        ans += temp * datatable[found_i - i // 2][i + 1]
        # print(datatable[found_i - i // 2][i + 1])
    return ans, msg


x = Symbol("x")
mn_min = -100
mx_max = 100
N_MIN = 2
N_MAX = 20

functions = list()
functions.append(Function(x ** 3 + 2 * x ** 2 - 5 * x - 6, "x^3 + 2x^2 - 5x - 6"))
functions.append(Function(sympy.sin(x), "sin(x)"))
functions.append(Function(x ** 2, "x^2"))

methods = list()
methods.append(Method(lagrange, "Многочлен Лагранжа"))
methods.append(Method(gauss, "Многочлен Гаусса"))
methods.append(Method(gauss2, "Многочлен Гаусса 2"))


def read_interval():
    while True:
        left = read_float(f"Введите левую границу из интервала ({mn_min};{mx_max}): ", mn_min, mx_max,
                          "Введено неправильное значение левой границы!")
        right = read_float(f"Введите левую границу из интервала ({left};{mx_max}): ", mn_min, mx_max,
                           "Введено неправильное значение правой границы!")
        if left >= right:
            print("Левая граница больше или равна правой, ошибочка, давай по новой, все фигня")
            continue
        else:
            return left, right


def read_int(text, mn, mx, error_msg):
    while True:
        try:
            val = int(input(text))
            if mn <= val <= mx:
                return val
            else:
                raise ValueError
        except ValueError:
            print(error_msg)


def read_float(text, mn, mx, error_msg) -> float:
    while True:
        try:
            val = float(input(text))
            if mn < val < mx:
                return val
            else:
                raise ValueError
        except ValueError:
            print(error_msg)


def read_two_numbers():
    text_in = input()
    if text_in == "":
        return None, None
    else:
        text_in = text_in.split()
        if len(text_in) == 2:
            return float(text_in[0]), float(text_in[1])
        else:
            raise ValueError


def read_table():
    print("Введите данные формата \"X Y\" в строчку, для окончания перечисления достаточно напечатать пустую строчку,"
          " без пробелов.")
    xx_list = list()
    yy_list = list()
    while True:
        try:
            xx, yy = read_two_numbers()
            if xx is None and yy is None:
                if len(xx_list) < N_MIN:
                    print("Куда пошел, ану сделай по чебуречески все, введи еще данные!!!!! Только " + str(
                        len(xx_list)) + " ввел")
                else:
                    break
            else:
                if xx_list.count(xx):
                    print(f"Такой x = {'{:.3f}'.format(xx)} уже есть, иди в пень! ")
                else:
                    xx_list.append(xx)
                    yy_list.append(yy)
        except ValueError:
            print("Введен неверный формат данных, попробуйте еще раз.")
    return xx_list, yy_list


def main():
    type_index = read_int("Выберите ввод данных: \n1. Готовая функция.\n2. Таблица данных.\n", 1, 2,
                          "Неправильный выбор, еще раз!")
    if type_index == 1:
        func_index = read_int(
            "Выберите функцию: \n" + "\n".join([f'{i + 1}. {functions[i].text}' for i in range(len(functions))]) + "\n",
            1, len(functions), "Неправильный выбор, еще раз!") - 1
        left, right = read_interval()
        amount = read_int(f"Введите кол-во узлов интерполяции [{N_MIN};{N_MAX}]: ", N_MIN, N_MAX,
                          "Ошибка ввода кол-ва узлов!")
        x_list = np.linspace(left, right, amount)
        y_list = list()
        for temp in x_list:
            y_list.append(functions[func_index].equation.subs(x, temp))
    else:
        x_list, y_list = read_table()
        x_list, y_list = zip(*sorted(zip(x_list, y_list)))
        left = x_list[0]
        right = x_list[-1]
        amount = len(x_list)

    x0 = read_float(f'Введите аргумент x0 ({"{:.3f}".format(left)};{"{:.3f}".format(right)}): ', left, right,
                    "Введен крингэ")

    print("\nИсходная таблица:\n" + tabulate([x_list, y_list], tablefmt='grid', floatfmt='7.3f') + "\n")

    allowed_meths = []
    results = []

    for method in methods:
        ans, msg = method.func(x_list, y_list, x0)
        if ans is None:
            print(method.text + ":", msg)
        else:
            allowed_meths.append(method)
            results.append(ans)
            print(method.text + ":", '{:.3f}'.format(ans))
    graph(x_list, y_list, allowed_meths, x0, results)


if "__main__" == __name__:
    main()
