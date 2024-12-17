import heapq


def parse_maze(filename):
    """Чтение лабиринта из файла."""
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze


def find_position(maze, target):
    """Поиск позиции символа (S или E) на карте."""
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == target:
                return x, y
    return None


def reindeer_maze(filename):
    """Решение задачи лабиринта с минимальной стоимостью."""
    # Чтение карты
    maze = parse_maze(filename)

    # Найти стартовую и конечную позиции
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')

    # Направления: Восток, Юг, Запад, Север
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_names = ['E', 'S', 'W', 'N']  # Названия направлений

    # Очередь с приоритетом для поиска пути
    queue = [(0, start[0], start[1], 0)]  # (стоимость, x, y, направление)
    visited = set()  # Храним посещённые состояния: (x, y, направление)

    while queue:
        cost, x, y, dir_idx = heapq.heappop(queue)

        # Если достигли конечной позиции
        if (x, y) == end:
            print(f"Минимальный счёт: {cost}")
            return cost

        # Если уже посещали это состояние
        if (x, y, dir_idx) in visited:
            continue
        visited.add((x, y, dir_idx))

        # Двигаемся вперёд в текущем направлении
        dx, dy = directions[dir_idx]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and maze[next_y][next_x] != '#':
            heapq.heappush(queue, (cost + 1, next_x, next_y, dir_idx))

        # Поворачиваемся на 90 градусов (влево и вправо)
        for turn in [-1, 1]:  # -1: влево, +1: вправо
            new_dir_idx = (dir_idx + turn) % 4
            heapq.heappush(queue, (cost + 1000, x, y, new_dir_idx))

    print("Путь не найден!")
    return None


if __name__ == "__main__":
    reindeer_maze("input.txt")
