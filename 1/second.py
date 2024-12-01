from collections import Counter


def read_input(file_path):
    """
    Считывает данные из файла и заполняет списки left_list и right_list.

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


def calculate_similarity_score(left_list, right_list):
    """
    Вычисляет коэффициент схожести между двумя списками.

    :param left_list: Список чисел (левая группа)
    :param right_list: Список чисел (правая группа)
    :return: Коэффициент схожести (целое число)
    """
    right_count = Counter(right_list)

    similarity_score = sum(number * right_count[number] for number in left_list)
    return similarity_score


def main():
    input_file = 'input.txt'

    left_list, right_list = read_input(input_file)

    similarity_score = calculate_similarity_score(left_list, right_list)

    print(f"Коэффициент схожести между списками: {similarity_score}")


if __name__ == "__main__":
    main()
