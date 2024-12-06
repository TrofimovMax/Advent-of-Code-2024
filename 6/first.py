from typing import Tuple, List


def simulate_guard_path(grid: List[str]):
    directions = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }
    direction_order = ["UP", "RIGHT", "DOWN", "LEFT"]

    current_position: Tuple[int, int] = (-1, -1)
    current_direction = "UP"

    for x, row in enumerate(grid):
        if "^" in row:
            current_position = (x, row.index("^"))
            break

    if current_position == (-1, -1):
        raise ValueError("Охранник не найден на карте.")

    visited_positions = set()
    visited_positions.add(current_position)

    rows, cols = len(grid), len(grid[0])
    obstacles = set(
        (x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == "#"
    )

    print(f"Начальная позиция: {current_position}")

    while True:
        x, y = current_position
        dx, dy = directions[current_direction]
        next_position = (x + dx, y + dy)

        if next_position[0] < 0 or next_position[1] < 0 or next_position[0] >= rows or next_position[1] >= cols:
            print("Охранник покинул карту.")
            break

        if next_position in obstacles:
            print(f"Препятствие на пути: {next_position}. Поворот направо.")
            current_direction = direction_order[(direction_order.index(current_direction) + 1) % 4]
        else:
            current_position = next_position
            visited_positions.add(current_position)

    print(f"Количество уникальных позиций, посещенных охранником: {len(visited_positions)}")
    return len(visited_positions)


def parse_input(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def run_guard_simulation(filename: str):
    grid = parse_input(filename)
    result = simulate_guard_path(grid)
    print(f"Результат для файла {filename}: {result}")


if __name__ == "__main__":
    run_guard_simulation("input.txt")
