class Node:
    def __init__(self, value, x, y):
        self.value = value  # Value of the cell ('#', '.', 'O', '@', '[', ']')
        self.x = x          # X-coordinate
        self.y = y          # Y-coordinate
        self.up = None      # Pointer to the node above
        self.down = None    # Pointer to the node below
        self.left = None    # Pointer to the node to the left
        self.right = None   # Pointer to the node to the right


def parse_file(filename):
    """Parse the input file into a warehouse map and a movement stack."""
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    warehouse_map = []
    moves = ""
    is_map = True

    for line in lines:
        if not line.strip():
            is_map = False
            continue

        if is_map:
            warehouse_map.append(list(line))
        else:
            moves += line.strip()

    return warehouse_map, moves


def scale_warehouse(warehouse_map):
    """Scale the warehouse map for part two."""
    scaled_map = []
    for row in warehouse_map:
        scaled_row = []
        for cell in row:
            if cell == '#':
                scaled_row.extend(['#', '#'])
            elif cell == 'O':
                scaled_row.extend(['[', ']'])
            elif cell == '.':
                scaled_row.extend(['.', '.'])
            elif cell == '@':
                scaled_row.extend(['@', '.'])
        scaled_map.append(scaled_row)
    return scaled_map


def build_doubly_linked_list(warehouse_map):
    """Build a doubly linked list representation of the warehouse map."""
    nodes = []
    for y, row in enumerate(warehouse_map):
        node_row = []
        for x, value in enumerate(row):
            node_row.append(Node(value, x, y))
        nodes.append(node_row)

    # Link nodes together
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            if y > 0:
                node.up = nodes[y - 1][x]
            if y < len(nodes) - 1:
                node.down = nodes[y + 1][x]
            if x > 0:
                node.left = row[x - 1]
            if x < len(row) - 1:
                node.right = row[x + 1]

    return nodes


def find_robot_position(nodes):
    """Find the robot's starting position."""
    for row in nodes:
        for node in row:
            if node.value == '@':
                return node


def print_warehouse(nodes):
    """Print the current state of the warehouse."""
    for row in nodes:
        print("".join(node.value for node in row))


def move_robot(robot, direction):
    """Move the robot and push boxes as needed."""
    direction_map = {
        '<': lambda node: node.left,
        '>': lambda node: node.right,
        '^': lambda node: node.up,
        'v': lambda node: node.down,
    }

    next_node = direction_map[direction](robot)

    # If the next node is a wall, robot cannot move
    if not next_node or next_node.value == '#':
        return robot

    # Handle movement and pushing boxes
    current = robot
    while next_node:
        if next_node.value == '.':
            # Swap robot position with '.'
            current.value, next_node.value = next_node.value, current.value
            return next_node
        elif next_node.value == '[':
            # Look ahead to check if the box can be pushed
            trail = []
            after_next = next_node
            while after_next and after_next.value == '[':
                trail.append(after_next)
                after_next = direction_map[direction](after_next)

            if after_next and after_next.value == '.':
                # Push all boxes forward
                for box in reversed(trail):
                    direction_map[direction](box).value = '['
                    box.value = '.'

                # Move robot
                after_next.value = '['
                next_node.value = '@'
                current.value = '.'
                return next_node
            break  # Cannot push further
        elif next_node.value == '#':
            # Wall, stop
            break

        current = next_node
        next_node = direction_map[direction](current)

    return robot  # If no movement was possible, return original position


def calculate_gps_sum(nodes):
    """Calculate the GPS sum of all boxes."""
    gps_sum = 0
    for row in nodes:
        for node in row:
            if node.value == '[':
                gps_sum += 100 * node.y + node.x
    return gps_sum


def warehouse_woes(filename: str):
    # Parse the file
    warehouse_map, moves = parse_file(filename)

    # Scale the warehouse map for part two
    scaled_map = scale_warehouse(warehouse_map)

    # Build the doubly linked list
    nodes = build_doubly_linked_list(scaled_map)

    # Find the robot's starting position
    robot = find_robot_position(nodes)

    # Execute the moves
    for move in moves:
        print(f"Move {move}:")
        print_warehouse(nodes)
        robot = move_robot(robot, move)
        print()

    # Calculate the GPS sum of all boxes
    gps_sum = calculate_gps_sum(nodes)
    print(f"Sum of all boxes' GPS coordinates: {gps_sum}")
    return gps_sum


if __name__ == "__main__":
    warehouse_woes("__input.txt")
