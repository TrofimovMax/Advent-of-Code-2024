from collections import defaultdict
from math import gcd
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

    # Для каждой частоты с 2 и более антеннами формируем линии и добавляем все точки на этих линиях
    for freq, positions in antennas_by_freq.items():
        if len(positions) < 2:
            # Если антенна одна, она не образует антиноды
            continue

        # Перебираем все пары антенн одинаковой частоты
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            dx = x2 - x1
            dy = y2 - y1
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # Чтобы не дублировать линии для пары (A,B) и (B,A), можно нормализовать направление:
            # Например, всегда делать dx, dy так, чтобы dx > 0 или dx=0 и dy > 0
            # Это не обязательно, так как множество точек set() защитит от дубликатов.
            # Но для стабильности нормализуем:
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            # Пройдём по линии в обе стороны от точки (x1, y1)
            # Вперёд по направлению (dx, dy)
            cx, cy = x1, y1
            while 0 <= cx < width and 0 <= cy < height:
                unique_antinodes.add((cx, cy))
                cx += dx
                cy += dy

            # Назад по направлению (-dx, -dy)
            cx, cy = x1, y1
            while 0 <= cx < width and 0 <= cy < height:
                unique_antinodes.add((cx, cy))
                cx -= dx
                cy -= dy

    # Выводим количество уникальных антинод в пределах карты
    print(f"Общее количество уникальных антинод: {len(unique_antinodes)}")


if __name__ == "__main__":
    resonant_collinearity("_input.txt")
    resonant_collinearity("input.txt")
