from typing import Tuple, List

def parse_input(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.rstrip('\n') for line in file]

def find_guard_start(grid: List[str]):
    for x, row in enumerate(grid):
        if "^" in row:
            return (x, row.index("^")), "UP"
        if ">" in row:
            return (x, row.index(">")), "RIGHT"
        if "v" in row:
            return (x, row.index("v")), "DOWN"
        if "<" in row:
            return (x, row.index("<")), "LEFT"
    raise ValueError("Охранник не найден.")

def simulate_guard_with_loop_check(grid: List[str], added_obstacle: Tuple[int,int] = None) -> str:
    """
    Симулируем движение охранника.
    Если added_obstacle задан, то добавляем препятствие в эту позицию.
    Возвращает:
    - "OUT": если охранник вышел за пределы карты
    - "LOOP": если обнаружен цикл
    """

    directions = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }
    direction_order = ["UP", "RIGHT", "DOWN", "LEFT"]

    start_position, start_direction = find_guard_start(grid)

    # Преобразуем grid в список списков для удобства
    grid_list = [list(row) for row in grid]

    # Если есть добавленное препятствие
    if added_obstacle:
        ox, oy = added_obstacle
        grid_list[ox][oy] = '#'

    # Возвращаем обратно в строковый формат для определения препятствий
    modified_grid = [''.join(r) for r in grid_list]

    rows, cols = len(modified_grid), len(modified_grid[0])

    obstacles = {(x, y) for x, row in enumerate(modified_grid) for y, cell in enumerate(row) if cell == "#"}

    current_position = start_position
    current_direction = start_direction

    # Отслеживаем состояния (позиция, направление) для обнаружения цикла
    seen_states = set()
    seen_states.add((current_position, current_direction))

    while True:
        x, y = current_position
        dx, dy = directions[current_direction]
        next_position = (x + dx, y + dy)

        # Выход за границы карты
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            return "OUT"

        if next_position in obstacles:
            # Поворот направо
            current_direction = direction_order[(direction_order.index(current_direction) + 1) % 4]
        else:
            # Шаг вперед
            current_position = next_position

        state = (current_position, current_direction)
        if state in seen_states:
            # Обнаружен цикл
            return "LOOP"
        seen_states.add(state)


def run_guard_simulation(filename: str):
    grid = parse_input(filename)
    rows, cols = len(grid), len(grid[0])

    # Начальная позиция охранника
    start_position, start_direction = find_guard_start(grid)

    # Ищем все позиции, где можно разместить препятствие
    # Препятствием не может быть:
    # - Начальная позиция охранника
    # - Позиции где уже есть '#'
    # - Позиции вне карты

    obstacles = {(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == "#"}
    loop_positions_count = 0

    for x in range(rows):
        for y in range(cols):
            if (x, y) != start_position and (x, y) not in obstacles:
                # Пробуем поставить препятствие
                result = simulate_guard_with_loop_check(grid, (x, y))
                if result == "LOOP":
                    loop_positions_count += 1

    print(f"Количество позиций для установки препятствия, приводящих к циклу: {loop_positions_count}")
    return loop_positions_count


if __name__ == "__main__":
    run_guard_simulation("input.txt")
