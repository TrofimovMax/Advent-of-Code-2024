def hoof_it(filename: str):
    # Считываем карту
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]

    rows, cols = len(grid), len(grid[0])
    heights = [[int(ch) for ch in row] for row in grid]

    # Найдём все стартовые точки (высота 0)
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if heights[r][c] == 0]

    # Направления: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def reachable_heights_from(start_r, start_c):
        # reachable_positions[h] будет хранить множество достижимых позиций высоты h
        reachable_positions = [set() for _ in range(10)]
        reachable_positions[0].add((start_r, start_c))

        # Для каждой высоты h находим достижимые позиции высоты h+1
        for h in range(9):
            for (r, c) in reachable_positions[h]:
                for nr, nc in neighbors(r, c):
                    if heights[nr][nc] == h + 1:
                        reachable_positions[h+1].add((nr, nc))

        # Вернём все достижимые позиции высоты 9
        return reachable_positions[9]

    # Считаем сумму оценок всех стартовых точек
    total_score = 0
    for (tr, tc) in trailheads:
        reachable_9 = reachable_heights_from(tr, tc)
        total_score += len(reachable_9)

    print(f"Сумма оценок всех стартовых точек для файла {filename}: {total_score}")


if __name__ == "__main__":
    hoof_it("_input.txt")  # Ожидается 36
    hoof_it("input.txt")
