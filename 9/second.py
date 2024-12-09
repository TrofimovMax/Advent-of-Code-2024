def disk_fragmenter(filename: str):
    with open(filename, 'r') as f:
        data = ''.join(ch for line in f for ch in line.strip() if ch.isdigit())

    # Преобразуем строку в список чисел, указывающих длины файлов и свободных промежутков
    lengths = list(map(int, data))
    blocks = []
    file_id = 0
    is_file = True  # True - следующий длина для файла, False - для свободного места

    # Формируем из длин список блоков: None для пустых, число (file_id) для файлов
    for length in lengths:
        if is_file:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend([None] * length)
        is_file = not is_file

    total_files = file_id

    def find_free_runs():
        """Находит все непрерывные отрезки свободных блоков (None)."""
        free_runs = []
        start = None
        for i, b in enumerate(blocks):
            if b is None:
                if start is None:
                    start = i
            else:
                if start is not None:
                    free_runs.append((start, i - 1))
                    start = None
        if start is not None:
            free_runs.append((start, len(blocks) - 1))
        return free_runs

    # Перемещаем файлы по одному, начиная с максимального ID
    for fid in range(total_files - 1, -1, -1):
        positions = [i for i, b in enumerate(blocks) if b == fid]
        if not positions:
            continue

        file_start = min(positions)
        file_end = max(positions)
        file_length = file_end - file_start + 1

        # Ищем подходящий свободный участок слева от файла
        free_runs = find_free_runs()
        suitable_run = None
        # Ищем самый левый подходящий отрезок
        # Условие: отрезок (fs, fe) должен быть полностью слева от file_start и
        # иметь длину не меньше длины файла.
        # "Слева от файла" означает fe < file_start (отрезок заканчивается до начала файла)
        for (fs, fe) in free_runs:
            run_length = fe - fs + 1
            if run_length >= file_length and fe < file_start:
                suitable_run = (fs, fe)
                break

        if suitable_run is not None:
            fs, fe = suitable_run
            for i in range(file_length):
                blocks[fs + i] = fid
            for i in range(file_start, file_end + 1):
                blocks[i] = None

    checksum = 0
    for i, b in enumerate(blocks):
        if b is not None:
            checksum += i * b

    print(f"Контрольная сумма: {checksum}")


if __name__ == "__main__":
    disk_fragmenter("_input_2.txt")
    disk_fragmenter("input.txt")
