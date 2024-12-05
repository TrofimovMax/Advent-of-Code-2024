def parse_input(data):
    rules_section, updates_section = data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates


def is_update_valid(update, rules):
    page_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_indices and y in page_indices:
            if page_indices[x] > page_indices[y]:
                return False
    return True


def reorder_update(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1

    queue = deque(page for page in update if in_degree[page] == 0)
    ordered_update = []

    while queue:
        current = queue.popleft()
        ordered_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update


def find_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]


def run_print_queue(filename):
    with open(filename, "r") as file:
        data = file.read()

    rules, updates = parse_input(data)
    invalid_updates = []
    total_middle_pages = 0

    for update in updates:
        if is_update_valid(update, rules):
            continue
        else:
            reordered = reorder_update(update, rules)
            total_middle_pages += find_middle_page(reordered)
            invalid_updates.append(reordered)

    print(f"Количество некорректных обновлений, исправленных: {len(invalid_updates)}")
    print(f"Сумма средних страниц исправленных обновлений: {total_middle_pages}")


def main():
    run_print_queue("_input.txt")
    run_print_queue("input.txt")


if __name__ == "__main__":
    main()
