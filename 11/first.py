def plutonian_pebbles(filename: str):
    with open(filename, 'r') as f:
        line = f.readline().strip()

    stones = line.split()
    stones = list(map(int, stones))

    def transform_stone(num: int) -> list:
        s = str(num)
        # Правило 1: Если число 0, заменяем на 1
        if num == 0:
            return [1]

        # Правило 2: Если число имеет чётное количество цифр, раскалываем на два камня
        length = len(s)
        if length % 2 == 0:
            half = length // 2
            left = int(s[:half])
            right = int(s[half:])
            return [left, right]

        # Правило 3: Иначе умножаем число на 2024
        new_num = num * 2024
        return [new_num]

    for _ in range(25):
        new_stones = []
        for st in stones:
            new_stones.extend(transform_stone(st))
        stones = new_stones

    # После 25 миганий выводим количество камней
    print(f"Количество камней после 25 миганий для файла {filename}: {len(stones)}")


if __name__ == "__main__":
    plutonian_pebbles("_input.txt")  # Ожидается 55312 после 25 миганий
    plutonian_pebbles("input.txt")
