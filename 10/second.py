def hoof_it(filename: str):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]

    rows, cols = len(grid), len(grid[0])
    heights = [[int(ch) for ch in row] for row in grid]

    # Направления: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # ways[h][r][c] — количество способов достичь клетки (r,c) высоты h
    # Для экономии памяти можно использовать список словарей или просто 2D массивы.
    # Здесь используем список словарей, где ключ — (r,c).
    ways = [dict() for _ in range(10)]

    # Инициализируем ways[0] для всех клеток высотой 0
    for r in range(rows):
        for c in range(cols):
            if heights[r][c] == 0:
                ways[0][(r, c)] = ways[0].get((r, c), 0) + 1

    # Функция для соседей
    def neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    # Заполняем ways для высот 1 до 9
    for h in range(9):
        for (r, c), count_ways in ways[h].items():
            # Ищем соседей с высотой h+1
            for nr, nc in neighbors(r, c):
                if heights[nr][nc] == h + 1:
                    ways[h+1][(nr, nc)] = ways[h+1].get((nr, nc), 0) + count_ways

    # Подсчитываем сумму всех способов добраться до высоты 9
    total_rating = sum(ways[9].values())

    print(f"Сумма рейтингов всех стартовых точек для файла {filename}: {total_rating}")


if __name__ == "__main__":
    hoof_it("_input.txt")  # ожидается 81
    hoof_it("input.txt")   # ожидается 1062
