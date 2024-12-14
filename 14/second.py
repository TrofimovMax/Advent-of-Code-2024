def display_map(robots, width, height):
    """Отображение карты роботов."""
    final_map = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        final_map[robot["p_y"]][robot["p_x"]] = "#"

    for row in final_map:
        print("".join(row))


def restroom_redoubt_with_easter_egg(filename):
    WIDTH, HEIGHT = 101, 103

    with open(filename, 'r') as f:
        data = f.read().strip().splitlines()

    robots = []
    for line in data:
        position_part, velocity_part = line.split()
        px, py = map(int, position_part[2:].split(","))
        vx, vy = map(int, velocity_part[2:].split(","))
        robots.append({"p_x": px, "p_y": py, "v_x": vx, "v_y": vy})

    tree_coordinates = []
    for level in range(10):
        start_x = 50 - level
        end_x = 50 + level
        y = level
        for x in range(start_x, end_x + 1):
            tree_coordinates.append((x, y))
    for y in range(10, 20):
        tree_coordinates.append((50, y))
    tree_coordinates = set(tree_coordinates)

    def normalize_positions(robots):
        """Преобразует позиции роботов в относительные координаты."""
        min_x = min(robot["p_x"] for robot in robots)
        min_y = min(robot["p_y"] for robot in robots)
        return {(robot["p_x"] - min_x, robot["p_y"] - min_y) for robot in robots}

    def is_christmas_tree(positions):
        """Проверяет, соответствует ли текущая конфигурация форме елки."""
        return positions == tree_coordinates

    seconds = 0

    while True:
        for robot in robots:
            robot["p_x"] += robot["v_x"]
            robot["p_y"] += robot["v_y"]

            if robot["p_x"] < 0:
                robot["p_x"] += WIDTH
            elif robot["p_x"] >= WIDTH:
                robot["p_x"] -= WIDTH

            if robot["p_y"] < 0:
                robot["p_y"] += HEIGHT
            elif robot["p_y"] >= HEIGHT:
                robot["p_y"] -= HEIGHT

        normalized_positions = normalize_positions(robots)
        if is_christmas_tree(normalized_positions):
            print(f"Рождественская елка сформирована через {seconds} секунд!")
            display_map(robots, WIDTH, HEIGHT)
            break

        seconds += 1


if __name__ == "__main__":
    restroom_redoubt_with_easter_egg("input.txt")
