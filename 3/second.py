import re


def parse_memory(file_path):
    """
    Считывает данные из файла и извлекает результаты для включённых инструкций mul(X,Y),
    учитывая условия do() и don't().

    :param file_path: Путь к файлу с данными.
    :return: Список результатов умножения для включённых инструкций mul(X,Y).
    """
    results = []
    pattern_mul = r"mul\((\d+),(\d+)\)"
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"
    is_enabled = True

    with open(file_path, 'r') as file:
        for line in file:
            instructions = re.split(r"(?=do\(\)|don't\(\)|mul\(\d+,\d+\))", line)
            for instr in instructions:
                if re.match(pattern_dont, instr):
                    is_enabled = False
                elif re.match(pattern_do, instr):
                    is_enabled = True
                elif is_enabled:
                    match = re.match(pattern_mul, instr)
                    if match:
                        x, y = map(int, match.groups())
                        results.append(x * y)

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
    print(f"Общая сумма результатов умножений (с учётом условий): {total}")


if __name__ == "__main__":
    main()
