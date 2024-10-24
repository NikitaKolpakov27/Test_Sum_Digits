# Получаем сумму цифр в строке
def get_sum_digit(str_num):

    digit_sum = 0
    for i in str_num:

        # В случае с отрицательным числом, следующую цифру не рассматриваем
        # (т.к. она уже была задействована в начале цикла)
        if str_num[0] == '-' and i == str_num[1]:
            continue

        # Обрабатываем ситуацию с отрицательным числом
        if i == '-':
            neg_num = int(i + str_num[1])
            digit_sum += neg_num
            continue

        digit_sum += int(i)

    return digit_sum

# Получаем ключ соответствующий наибольшому значению суммы цифр
def get_max_sum_number(mapa):
    for i in mapa.items():
        if i[1] == max(mapa.values()):
            return i[0]


def main_func():
    mapa = {}

    while True:

        try:
            user_input = input()

            if int(user_input) == 0:
                break

        except ValueError:
            print("Нужно вводить только целые числа!")
            continue

        int_user_input = int(user_input)
        mapa[int_user_input] = get_sum_digit(user_input)

    # Выводим в консоль число с максимальной суммой цифр в нем
    print("Ответ:", get_max_sum_number(mapa))
    return get_max_sum_number(mapa)


if __name__ == "__main__":
    main_func()
