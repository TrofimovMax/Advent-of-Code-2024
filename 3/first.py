import re


def parse_memory(file_path):
    """
    Считывает данные из файла и извлекает корректные инструкции mul(X,Y).

    :param file_path: Путь к файлу с данными.
    :return: Список результатов умножения для каждой инструкции mul(X,Y).
    """
    results = []
    pattern = r"mul\((\d+),(\d+)\)"

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for x, y in matches:
                results.append(int(x) * int(y))

    return results


def calculate_total(results):
    """
    Вычисляет общую сумму результатов умножений.

    :param results: Список результатов умножения.
    :return: Общая сумма.
    """
    return sum(results)


def main():
    input_file = 'input.txt'
    results = parse_memory(input_file)
    total = calculate_total(results)
    print(f"Общая сумма результатов умножений: {total}")


if __name__ == "__main__":
    main()
