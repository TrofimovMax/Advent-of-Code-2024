def restroom_redoubt(filename):
    # Размеры пространства
    WIDTH, HEIGHT = 101, 103
    QUADRANT_WIDTH = WIDTH // 2
    QUADRANT_HEIGHT = HEIGHT // 2

    # Считываем входные данные
    with open(filename, 'r') as f:
        data = f.read().strip().splitlines()

    # Парсим входные данные в список словарей
    robots = []
    for line in data:
        try:
            position_part, velocity_part = line.split()
            px, py = map(int, position_part[2:].split(","))
            vx, vy = map(int, velocity_part[2:].split(","))
            robots.append({"p_x": px, "p_y": py, "v_x": vx, "v_y": vy})
        except ValueError:
            print(f"Ошибка обработки строки: {line}")
            continue

    # Симуляция движения роботов
    for _ in range(100):  # 100 секунд симуляции
        for robot in robots:
            robot["p_x"] += robot["v_x"]
            robot["p_y"] += robot["v_y"]

            # Циклическое перемещение (телепортация)
            if robot["p_x"] < 0:
                robot["p_x"] += WIDTH
            elif robot["p_x"] >= WIDTH:
                robot["p_x"] -= WIDTH

            if robot["p_y"] < 0:
                robot["p_y"] += HEIGHT
            elif robot["p_y"] >= HEIGHT:
                robot["p_y"] -= HEIGHT

    # Построение итоговой карты после 100 секунд
    final_map = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
        final_map[robot["p_y"]][robot["p_x"]] += 1

    # Отображение карты
    print("Карта после 100 секунд:")
    for row in final_map:
        print("".join(str(cell) if cell > 0 else "." for cell in row))

    # Подсчёт количества роботов в квадрантах
    quadrants = [0, 0, 0, 0]  # Верхний левый, верхний правый, нижний левый, нижний правый

    for y in range(HEIGHT):
        for x in range(WIDTH):
            count = final_map[y][x]
            if count == 0:
                continue
            if x == QUADRANT_WIDTH or y == QUADRANT_HEIGHT:
                # Игнорируем роботов на границах квадрантов
                continue
            if x < QUADRANT_WIDTH and y < QUADRANT_HEIGHT:
                quadrants[0] += count
            elif x >= QUADRANT_WIDTH and y < QUADRANT_HEIGHT:
                quadrants[1] += count
            elif x < QUADRANT_WIDTH and y >= QUADRANT_HEIGHT:
                quadrants[2] += count
            elif x >= QUADRANT_WIDTH and y >= QUADRANT_HEIGHT:
                quadrants[3] += count

    # Вычисляем показатель безопасности
    safety_factor = 1
    for count in quadrants:
        if count > 0:
            safety_factor *= count  # Учитываем только ненулевые значения

    print(f"Квадранты: {quadrants}")
    print(f"Показатель безопасности: {safety_factor}")
    return safety_factor


if __name__ == "__main__":
    restroom_redoubt("input.txt")
