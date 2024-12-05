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


def find_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]


def run_print_queue(filename):
    with open(filename, "r") as file:
        data = file.read()

    rules, updates = parse_input(data)
    valid_updates = []
    total_middle_pages = 0

    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
            total_middle_pages += find_middle_page(update)

    print(f"Количество корректных обновлений: {len(valid_updates)}")
    print(f"Сумма средних страниц: {total_middle_pages}")


def main():
    run_print_queue("_input.txt")
    run_print_queue("input.txt")


if __name__ == "__main__":
    main()
