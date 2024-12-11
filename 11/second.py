import time
from collections import Counter


def plutonian_pebbles_optimized(filename: str):
    start_time = time.time()

    # Считываем исходные данные
    with open(filename, 'r') as f:
        line = f.readline().strip()

    stones = list(map(int, line.split()))

    # Используем Counter для подсчёта количества одинаковых камней
    stone_counts = Counter(stones)

    for _ in range(75):
        new_stone_counts = Counter()

        # Применяем правила ко всем текущим камням
        for stone, count in stone_counts.items():
            if stone == 0:
                # Правило 1: Камень 0 заменяется на 1
                new_stone_counts[1] += count
            else:
                stone_str = str(stone)
                if len(stone_str) % 2 == 0:
                    # Правило 2: Чётное количество цифр, делим на два камня
                    half = len(stone_str) // 2
                    left = int(stone_str[:half])
                    right = int(stone_str[half:])
                    new_stone_counts[left] += count
                    new_stone_counts[right] += count
                else:
                    # Правило 3: Умножаем на 2024
                    new_stone_counts[stone * 2024] += count

        # Обновляем состояния камней
        stone_counts = new_stone_counts

    # Считаем общее количество камней
    total_stones = sum(stone_counts.values())

    print(f"Количество камней после 75 миганий для файла {filename}: {total_stones}")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.4f} секунд")


if __name__ == "__main__":
    # plutonian_pebbles_optimized("_input.txt")
    plutonian_pebbles_optimized("input.txt")
