from collections import defaultdict
from itertools import combinations


def resonant_collinearity(filename: str):
    # Считываем карту
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    height = len(lines)
    width = len(lines[0]) if height > 0 else 0

    # Собираем антенны по их частоте
    # Ключ - символ (частота), значение - список координат (x,y)
    antennas_by_freq = defaultdict(list)
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch != '.':
                antennas_by_freq[ch].append((x, y))

    unique_antinodes = set()

    # Для каждой частоты, у которой >= 2 антенн, находим пары антенн
    # и вычисляем антиноды.
    for freq, positions in antennas_by_freq.items():
        if len(positions) < 2:
            continue

        # Перебираем все пары антенн одинаковой частоты
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            # Вычисляем две точки-антиноды

            # Первая антинода: P1 = 2*A - B
            # Если A=(x1,y1), B=(x2,y2), то P1=(2*x1 - x2, 2*y1 - y2)
            p1x = 2 * x1 - x2
            p1y = 2 * y1 - y2

            # Вторая антинода: P2 = 2*B - A
            # P2 = (2*x2 - x1, 2*y2 - y1)
            p2x = 2 * x2 - x1
            p2y = 2 * y2 - y1

            # Проверяем, что антиноды лежат в пределах карты
            if 0 <= p1x < width and 0 <= p1y < height:
                unique_antinodes.add((p1x, p1y))
            if 0 <= p2x < width and 0 <= p2y < height:
                unique_antinodes.add((p2x, p2y))

    # Выводим количество уникальных антинод в пределах карты
    print(f"Общее количество уникальных антинод: {len(unique_antinodes)}")


if __name__ == "__main__":
    resonant_collinearity("_input.txt")
    resonant_collinearity("input.txt")
