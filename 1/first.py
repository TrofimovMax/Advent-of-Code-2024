def calculate_total_distance(left_list, right_list):
    """
    Вычисляет общее расстояние между двумя списками,
    где элементы сопоставляются по их возрастанию.

    :param left_list: Список целых чисел (левая группа)
    :param right_list: Список целых чисел (правая группа)
    :return: Общее расстояние (целое число)
    """
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    total_distance = sum(abs(left - right) for left, right in zip(left_list_sorted, right_list_sorted))
    return total_distance


def read_input(file_path):
    """
    Считывает данные из файла и разделяет их на два списка: левый и правый.

    :param file_path: Путь к файлу с данными.
    :return: Кортеж из двух списков: left_list и right_list.
    """
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 2:
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))

    return left_list, right_list


def main():
    input_file = 'input.txt'
    left_list, right_list = read_input(input_file)

    total_distance = calculate_total_distance(left_list, right_list)

    print(f"Общее расстояние между списками: {total_distance}")


if __name__ == "__main__":
    main()
