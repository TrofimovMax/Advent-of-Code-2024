from sympy import symbols, Eq, solve

def solve_claw_machines(filename: str):
    x, y = symbols('x y')

    with open(filename, 'r') as f:
        data = f.read().strip().split("\n\n")

    total_tokens = 0
    prizes_won = 0

    # Смещение для координат призов
    offset = 10_000_000_000_00

    for idx, machine in enumerate(data):
        lines = machine.splitlines()

        # Извлекаем параметры кнопок и призов
        ax, ay = map(int, lines[0].split(":")[1].replace("X+", "").replace("Y+", "").split(","))
        bx, by = map(int, lines[1].split(":")[1].replace("X+", "").replace("Y+", "").split(","))
        px, py = map(int, lines[2].split(":")[1].replace("X=", "").replace("Y=", "").split(","))

        # Применяем смещение
        px += offset
        py += offset

        # Уравнения для X и Y
        eq_x = Eq(ax * x + bx * y, px)
        eq_y = Eq(ay * x + by * y, py)

        print(f"\nМашина {idx + 1}: решаем для X ({eq_x}) и Y ({eq_y})")

        # Решаем уравнение для X
        solutions_x = solve(eq_x, x)
        if not solutions_x:
            print("  Нет решений для X.")
            continue

        found_solution = False
        min_cost = float('inf')

        # Перебираем возможные значения y для проверки уравнения Y
        for sol in solutions_x:
            for y_val in range(0, 101):
                x_val = sol.subs(y, y_val)
                if isinstance(x_val, (int, float)) and float(x_val).is_integer():
                    x_val = int(x_val)
                    if eq_y.subs({x: x_val, y: y_val}) == 0:
                        cost = 3 * x_val + y_val
                        if cost < min_cost:
                            min_cost = cost
                        found_solution = True

        if found_solution:
            prizes_won += 1
            total_tokens += min_cost
            print(f"  Найдено решение с минимальной стоимостью: {min_cost} токенов")
        else:
            print("  Решений для Y нет.")

    print(f"\nМаксимальное количество призов: {prizes_won}")
    print(f"Минимальное количество жетонов: {total_tokens}")


if __name__ == "__main__":
    solve_claw_machines("_input.txt")
