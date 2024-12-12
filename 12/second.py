def garden_groups(filename: str):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        grid = f.read().splitlines()

    grid = [row for row in grid if row]

    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)]

    def neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            yield nr, nc

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def find_region(r, c):
        plant_type = grid[r][c]
        stack = [(r, c)]
        visited[r][c] = True
        region_coords = []
        while stack:
            cr, cc = stack.pop()
            region_coords.append((cr, cc))
            for nr, nc in neighbors(cr, cc):
                if in_bounds(nr, nc) and not visited[nr][nc] and grid[nr][nc] == plant_type:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        return region_coords

    def count_sides(region_coords):
        region_set = set(region_coords)
        side_count = 0

        for (cr, cc) in region_coords:
            for nr, nc in neighbors(cr, cc):
                if not in_bounds(nr, nc) or (nr, nc) not in region_set:
                    side_count += 1

        return side_count

    def calculate_area(region_coords):
        return len(region_coords)

    total_cost = 0
    details = []

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region_coords = find_region(r, c)
                area = calculate_area(region_coords)
                sides = count_sides(region_coords)
                cost = area * sides
                total_cost += cost
                details.append((grid[r][c], area, sides, cost))

    print(f"Суммарная стоимость для файла {filename}: {total_cost}")
    print("Детали регионов:")
    for plant, area, sides, cost in details:
        print(f"Растение {plant}: Площадь {area}, Стороны {sides}, Стоимость {cost}")


if __name__ == "__main__":
    garden_groups("_input.txt")  # ожидается 1206
