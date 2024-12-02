def is_safe_report(report):
    """
    Проверяет, является ли отчёт безопасным.

    :param report: Список чисел, представляющих уровни в отчёте.
    :return: True, если отчёт безопасный, иначе False.
    """
    if len(report) < 2:
        return False

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= diff <= 3 for diff in differences):
        return True
    if all(-3 <= diff <= -1 for diff in differences):
        return True

    return False


def is_safe_with_dampener(report):
    """
    Проверяет, является ли отчёт безопасным с учётом Проблемо-Подавителя.

    :param report: Список чисел, представляющих уровни в отчёте.
    :return: True, если отчёт становится безопасным при удалении одного уровня, иначе False.
    """
    if is_safe_report(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True

    return False


def read_reports(file_path):
    """
    Считывает отчёты из файла.

    :param file_path: Путь к файлу с отчётами.
    :return: Список отчётов, где каждый отчёт — это список чисел.
    """
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))
    return reports


def count_safe_reports_with_dampener(reports):
    """
    Считает количество безопасных отчётов с учётом Проблемо-Подавителя.

    :param reports: Список отчётов (списков чисел).
    :return: Количество безопасных отчётов.
    """
    return sum(is_safe_with_dampener(report) for report in reports)


def main():
    input_file = 'input.txt'
    reports = read_reports(input_file)
    safe_count = count_safe_reports_with_dampener(reports)
    print(f"Количество безопасных отчётов (с учётом Проблемо-Подавителя): {safe_count}")


if __name__ == "__main__":
    main()
