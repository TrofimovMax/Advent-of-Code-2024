from itertools import product


def parse_input(filename: str):
    """Считывает входные данные из файла и преобразует их в список."""
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                target, numbers = line.split(':')
                target = int(target.strip())
                numbers = list(map(int, numbers.strip().split()))
                equations.append((target, numbers))
    return equations


def evaluate_equation(numbers, operators):
    """Вычисляет значение уравнения с заданными числами и операторами."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


def can_calculate_target(target, numbers):
    """Проверяет, можно ли получить целевое значение, расставив операторы."""
    operator_choices = ['+', '*']
    for operators in product(operator_choices, repeat=len(numbers) - 1):
        if evaluate_equation(numbers, operators) == target:
            return True
    return False


def calculate_total_valid_targets(equations):
    """Вычисляет сумму всех целевых значений, которые можно получить."""
    total = 0
    for target, numbers in equations:
        if can_calculate_target(target, numbers):
            total += target
    return total


def run_bridge_repair(filename: str):
    """Основная функция для чтения данных, вычисления и вывода результата."""
    equations = parse_input(filename)
    total = calculate_total_valid_targets(equations)
    print(f"Общая сумма валидных целевых значений: {total}")


if __name__ == "__main__":
    run_bridge_repair("_input.txt")
    run_bridge_repair("input.txt")
