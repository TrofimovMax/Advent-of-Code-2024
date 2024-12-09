def disk_fragmenter(filename: str):
    # Считываем все строки из файла, убираем пробелы, переносы строк
    # и игнорируем все нецифровые символы, включая точки.
    with open(filename, 'r') as f:
        data = ''.join(ch for line in f for ch in line.strip() if ch.isdigit())

    # Преобразуем строку в список чисел
    lengths = list(map(int, data))
    blocks = []
    file_id = 0
    is_file = True

    # Заполняем массив блоков: None для пустого места и file_id для файлов
    for length in lengths:
        if is_file:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend([None] * length)
        is_file = not is_file

    # Уплотнение: переносим самые правые файловые блоки в самые левые свободные места
    while True:
        try:
            leftmost_free = blocks.index(None)
        except ValueError:
            break

        rightmost_file = -1
        for i in range(len(blocks)-1, -1, -1):
            if blocks[i] is not None:
                rightmost_file = i
                break

        if rightmost_file <= leftmost_free:
            # Все файлы уже уплотнены
            break

        blocks[leftmost_free] = blocks[rightmost_file]
        blocks[rightmost_file] = None

    checksum = 0
    for i, b in enumerate(blocks):
        if b is not None:
            checksum += i * b

    print(f"Контрольная сумма: {checksum}")


if __name__ == "__main__":
    disk_fragmenter("_input.txt")
    disk_fragmenter("input.txt")
