def count_x_mas(grid):
    """
    Подсчитывает количество X-MAS в головоломке.

    :param grid: Список строк, представляющий головоломку.
    :return: Количество X-MAS.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Все шаблоны X-MAS
    patterns = [
        # Шаблон 1
        [
            ["M", "*", "*"],
            ["*", "A", "*"],
            ["*", "*", "S"]
        ],
        # Шаблон 2
        [
            ["S", "*", "*"],
            ["*", "A", "*"],
            ["*", "*", "M"]
        ],
        # Шаблон 3
        [
            ["*", "*", "M"],
            ["*", "A", "*"],
            ["S", "*", "*"]
        ],
        # Шаблон 4
        [
            ["*", "*", "S"],
            ["*", "A", "*"],
            ["M", "*", "*"]
        ],
    ]

    def matches_pattern(subgrid, pattern):
        """
        Проверяет, совпадает ли подокно с шаблоном.
        '*' в шаблоне означает, что в этой позиции может быть любой символ.
        """
        for i in range(3):
            for j in range(3):
                if pattern[i][j] != "*" and subgrid[i][j] != pattern[i][j]:
                    return False
        return True

    # Проходим по всем окнам 3x3
    for x in range(rows - 2):
        for y in range(cols - 2):
            # Извлекаем окно 3x3
            subgrid = [row[y:y + 3] for row in grid[x:x + 3]]

            # Проверяем только до первого совпадения
            if any(matches_pattern(subgrid, pattern) for pattern in patterns):
                count += 1

    return count


def run_ceres_search(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]

    print(f"\nАнализ файла: {filename}")
    for row in grid:
        print(row)

    total_x_mas = count_x_mas(grid)
    print(f"Количество X-MAS в головоломке: {total_x_mas}")


def main():
    run_ceres_search('_input_.txt')  # Ожидается: 2
    run_ceres_search('_input.txt')  # Ожидается: 9


if __name__ == "__main__":
    main()
