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


def find_blocking_byte(grid_size, bytes_positions):
    """Находит координаты первого байта, который блокирует путь."""
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for i, (x, y) in enumerate(bytes_positions):
        grid[y][x] = '#'
        if find_shortest_path(grid) == -1:
            return x, y  # Координаты байта, который блокирует путь

    return None  # Если путь не заблокирован


def ram_run(filename):
    """Выполняет задачу RAM Run."""
    bytes_positions = parse_input(filename)
    grid_size = 71  # Размер сетки (71x71 для задачи)

    blocking_byte = find_blocking_byte(grid_size, bytes_positions)

    if blocking_byte:
        print(f"Координаты первого байта, который блокирует путь: {blocking_byte[0]},{blocking_byte[1]}")
    else:
        print("Путь не заблокирован даже после всех байтов.")


if __name__ == "__main__":
    ram_run("input.txt")
