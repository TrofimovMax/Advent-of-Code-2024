def parse_word_search(file_path, word):
    """
    Подсчитывает количество вхождений слова в таблице поиска слов.

    :param file_path: Путь к файлу с таблицей.
    :param word: Слово для поиска.
    :return: Общее количество вхождений слова.
    """

    def count_word(grid, word, dx, dy):
        rows, cols, word_length = len(grid), len(grid[0]), len(word)
        return sum(
            all(
                0 <= x + k * dx < rows and
                0 <= y + k * dy < cols and
                grid[x + k * dx][y + k * dy] == word[k]
                for k in range(word_length)
            )
            for x in range(rows) for y in range(cols)
        )

    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]

    directions = [
        (0, 1),    # Горизонтально вправо
        (1, 0),    # Вертикально вниз
        (1, 1),    # Диагонально вправо вниз
        (1, -1),   # Диагонально вправо вверх
        (0, -1),   # Горизонтально влево
        (-1, 0),   # Вертикально вверх
        (-1, -1),  # Диагонально влево вверх
        (-1, 1)    # Диагонально влево вниз
    ]

    return sum(count_word(grid, word, dx, dy) for dx, dy in directions)


def main():
    input_file = 'input.txt'
    word = 'XMAS'
    total_count = parse_word_search(input_file, word)
    print(f"Количество вхождений слова {word}: {total_count}")


if __name__ == "__main__":
    main()
