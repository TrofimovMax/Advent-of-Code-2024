def garden_groups(filename: str):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]
    rows = len(grid)
    cols = len(grid[0])

    # Направления: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False]*cols for _ in range(rows)]

    def neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            yield nr, nc

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    total_cost = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Новый регион
                plant_type = grid[r][c]
                stack = [(r, c)]
                visited[r][c] = True
                region_coords = []

                # Поиск в глубину (DFS) для определения координат региона
                while stack:
                    cr, cc = stack.pop()
                    region_coords.append((cr, cc))
                    for nr, nc in neighbors(cr, cc):
                        if in_bounds(nr, nc) and not visited[nr][nc] and grid[nr][nc] == plant_type:
                            visited[nr][nc] = True
                            stack.append((nr, nc))

                # Подсчёт площади региона: количество участков
                area = len(region_coords)

                # Подсчёт периметра
                # Периметр — сумма сторон, не граничащих с тем же регионом
                perimeter = 0
                region_set = set(region_coords)
                for (cr, cc) in region_coords:
                    # Проверяем каждую из 4 сторон
                    for nr, nc in neighbors(cr, cc):
                        # Если сосед вне границ или сосед не в этом регионе
                        if not in_bounds(nr, nc) or (nr, nc) not in region_set:
                            perimeter += 1

                # Стоимость для этого региона
                cost = area * perimeter
                total_cost += cost

    print(f"Суммарная стоимость для файла {filename}: {total_cost}")


if __name__ == "__main__":
    garden_groups("_input.txt")  # ожидается 1930
    garden_groups("input.txt")
