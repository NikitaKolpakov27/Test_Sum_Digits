# Получаем сумму цифр в строке
def get_sum_digit(str_num):
    return sum(int(i) for i in str_num if i.isdigit())

# Получаем ключ соответствующий наибольшому значению суммы цифр
def get_max_sum_number(mapa):
    for i in mapa.items():
        if i[1] == max(mapa.values()):
            return i[0]


if __name__ == "__main__":
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
    final_click = input("Нажмите Enter, чтобы выйти")
