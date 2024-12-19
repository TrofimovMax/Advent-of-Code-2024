def parse_input(filename):
    """Читает входные данные из файла."""
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()
    return [tuple(map(int, line.split(','))) for line in lines]


def simulate_falling_bytes(grid_size, bytes_positions):
    """Создаёт сетку и симулирует падение байтов."""
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in bytes_positions:
        grid[y][x] = '#'
    return grid


def find_shortest_path(grid):
    """Находит кратчайший путь от (0,0) до (n-1,n-1)."""
    from collections import deque

    n = len(grid)
    start, end = (0, 0), (n - 1, n - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if grid[start[1]][start[0]] == '#' or grid[end[1]][end[0]] == '#':
        return -1

    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[ny][nx] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # Нет пути


def print_grid(grid):
    """Печатает текущую сетку."""
    for row in grid:
        print(''.join(row))


def ram_run(filename):
    """Выполняет задачу RAM Run."""
    bytes_positions = parse_input(filename)
    grid_size = 71  # Размер сетки (71x71 для задачи) 7 для _input

    # Симуляция падения первых 1024 байтов
    grid = simulate_falling_bytes(grid_size, bytes_positions[:1024])  # 12 для _input

    print("Состояние памяти после падения байтов:")
    print_grid(grid)

    steps = find_shortest_path(grid)
    if steps == -1:
        print("Нет доступного пути до выхода.")
    else:
        print(f"Минимальное количество шагов до выхода: {steps}")

    return steps


if __name__ == "__main__":
    ram_run("input.txt")
