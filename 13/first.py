from math import gcd


def extended_gcd(a, b):
    """Расширенный алгоритм Евклида для нахождения x, y в уравнении ax + by = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def solve_linear_diophantine(a, b, c, x_limit, y_limit):
    """Решение линейного диофантового уравнения ax + by = c с ограничениями на x и y."""
    g, x0, y0 = extended_gcd(a, b)
    if c % g != 0:
        return None  # Решений нет

    x0 *= c // g
    y0 *= c // g
    a //= g
    b //= g

    solutions = []

    # Перемещаемся вдоль решения (x0, y0) с шагами b и -a
    k_min = max((-x0) // b, (y0 - y_limit) // a)
    k_max = min((x_limit - x0) // b, y0 // a)

    for k in range(k_min, k_max + 1):
        x = x0 + k * b
        y = y0 - k * a
        if 0 <= x <= x_limit and 0 <= y <= y_limit:
            solutions.append((x, y))

    return solutions


def solve_claw_machines(filename: str):
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n\n")

    total_tokens = 0
    prizes_won = 0

    for machine in data:
        lines = machine.splitlines()

        # Обрабатываем строки для извлечения чисел после "X+" и "Y+"
        ax, ay = map(int, lines[0].split(":")[1].replace("X+", "").replace("Y+", "").split(","))
        bx, by = map(int, lines[1].split(":")[1].replace("X+", "").replace("Y+", "").split(","))
        px, py = map(int, lines[2].split(":")[1].replace("X=", "").replace("Y=", "").split(","))

        # Решаем диофантово уравнение для X
        x_solutions = solve_linear_diophantine(ax, bx, px, 100, 100)
        if x_solutions:
            min_cost = float('inf')
            for x, y in x_solutions:
                # Проверяем, совпадают ли Y
                if ay * x + by * y == py:
                    cost = 3 * x + 1 * y
                    min_cost = min(min_cost, cost)

            if min_cost != float('inf'):
                prizes_won += 1
                total_tokens += min_cost

    print(f"Максимальное количество призов: {prizes_won}")
    print(f"Минимальное количество жетонов: {total_tokens}")


if __name__ == "__main__":
    solve_claw_machines("_input.txt")
    solve_claw_machines("input.txt")