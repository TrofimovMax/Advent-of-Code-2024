def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == 'A':
                # Диагональ 1: верх-лево и низ-право
                chars_diag1 = {grid[x - 1][y - 1], grid[x + 1][y + 1]}
                # Диагональ 2: верх-право и низ-лево
                chars_diag2 = {grid[x - 1][y + 1], grid[x + 1][y - 1]}

                # Проверяем, что обе диагонали содержат {'M','S'}
                if chars_diag1 == {'M', 'S'} and chars_diag2 == {'M', 'S'}:
                    count += 1

    return count


def run_ceres_search(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]

    total_x_mas = count_x_mas(grid)
    print(f"Количество X-MAS в головоломке: {total_x_mas}")


def main():
    run_ceres_search('_input_.txt')  # Ожидается: 2
    run_ceres_search('_input.txt')  # Ожидается: 9
    run_ceres_search('input.txt')


if __name__ == "__main__":
    main()
