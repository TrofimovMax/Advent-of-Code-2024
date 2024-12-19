def parse_input(filename):
    """Читает входные данные из файла."""
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()

    towel_patterns = lines[0].split(', ')
    designs = lines[2:]
    return towel_patterns, designs


def can_form_design(towel_patterns, design):
    """Проверяет, можно ли собрать дизайн из доступных полотенец с помощью динамического программирования."""
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[n]


def linen_layout(filename):
    """Определяет количество возможных дизайнов."""
    towel_patterns, designs = parse_input(filename)

    possible_count = 0

    for design in designs:
        if can_form_design(towel_patterns, design):
            possible_count += 1

    print(f"Количество возможных дизайнов: {possible_count}")
    return possible_count


if __name__ == "__main__":
    linen_layout("input.txt")
