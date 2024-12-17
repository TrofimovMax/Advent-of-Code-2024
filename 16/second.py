import heapq

def parse_maze(filename):
    """Чтение лабиринта из файла."""
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def find_positions(maze, target):
    """Поиск всех позиций символа (S или E) на карте."""
    positions = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == target:
                positions.append((x, y))
    return positions

def reindeer_maze(filename):
    """Решение задачи лабиринта с минимальной стоимостью и определение лучших путей."""
    # Чтение карты
    maze = parse_maze(filename)

    # Найти стартовые и конечные позиции
    starts = find_positions(maze, 'S')
    ends = find_positions(maze, 'E')

    # Направления: Восток, Юг, Запад, Север
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Очередь с приоритетом для поиска пути
    best_path = set()
    for start in starts:
        for end in ends:
            queue = [(0, start[0], start[1], 0, [(start[0], start[1])])]  # (стоимость, x, y, направление, путь)
            visited = set()  # Храним посещённые состояния: (x, y, направление)
            current_path = set()

            while queue:
                cost, x, y, dir_idx, path = heapq.heappop(queue)

                # Если достигли конечной позиции
                if (x, y) == end:
                    current_path.update(path)
                    break

                # Если уже посещали это состояние
                if (x, y, dir_idx) in visited:
                    continue
                visited.add((x, y, dir_idx))

                # Двигаемся вперёд в текущем направлении
                dx, dy = directions[dir_idx]
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and maze[next_y][next_x] != '#':
                    heapq.heappush(queue, (cost + 1, next_x, next_y, dir_idx, path + [(next_x, next_y)]))

                # Поворачиваемся на 90 градусов (влево и вправо)
                for turn in [-1, 1]:  # -1: влево, +1: вправо
                    new_dir_idx = (dir_idx + turn) % 4
                    heapq.heappush(queue, (cost + 1000, x, y, new_dir_idx, path))

            best_path.update(current_path)

    # Обновление карты для второй части
    for y, row in enumerate(maze):
        for x, _ in enumerate(row):
            if (x, y) in best_path and maze[y][x] not in ('S', 'E'):
                maze[y][x] = 'O'

    # Вывод карты с отмеченными лучшими путями
    for row in maze:
        print("".join(row))

    print(f"Количество плиток, являющихся частью лучших маршрутов: {len(best_path)}")
    return len(best_path)

if __name__ == "__main__":
    reindeer_maze("__input.txt")