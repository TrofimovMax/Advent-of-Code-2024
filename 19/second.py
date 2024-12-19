def parse_input(filename):
    """Читает входные данные из файла."""
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()

    towel_patterns = lines[0].split(', ')
    designs = lines[2:]
    return towel_patterns, designs


def count_ways_to_form_design(towel_patterns, design):
    """Считает количество способов собрать дизайн из доступных полотенец с помощью динамического программирования."""
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[n]


def linen_layout(filename):
    """Считает общее количество способов для всех возможных дизайнов."""
    towel_patterns, designs = parse_input(filename)

    total_ways = 0

    for design in designs:
        ways = count_ways_to_form_design(towel_patterns, design)
        total_ways += ways
        print(f"Дизайн: {design}, Способы: {ways}")

    print(f"Общее количество способов: {total_ways}")
    return total_ways


if __name__ == "__main__":
    linen_layout("input.txt")
