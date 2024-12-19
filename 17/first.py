def parse_input(filename):
    """Чтение входных данных из файла."""
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()

    registers = {}
    program = []

    for line in lines:
        if line.startswith("Register A:"):
            registers['A'] = int(line.split(": ")[1])
        elif line.startswith("Register B:"):
            registers['B'] = int(line.split(": ")[1])
        elif line.startswith("Register C:"):
            registers['C'] = int(line.split(": ")[1])
        elif line.startswith("Program:"):
            program = list(map(int, line.split(": ")[1].split(",")))

    return registers, program


def emulate_3bit_computer(registers, program):
    """
    Эмулирует работу 3-битного компьютера.

    :param registers: Словарь начальных значений регистров {'A': int, 'B': int, 'C': int}.
    :param program: Список инструкций программы (список чисел).
    :return: Результат вывода программы (строка чисел, разделённых запятой).
    """
    A, B, C = registers['A'], registers['B'], registers['C']
    instruction_pointer = 0
    output = []

    def get_combo_value(operand):
        """Получить значение комбинированного операнда."""
        if operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand < 4:
            return operand
        else:
            raise ValueError(f"Недопустимый операнд: {operand}")

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv
            A //= 2 ** get_combo_value(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** get_combo_value(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** get_combo_value(operand))
        else:
            raise ValueError(f"Неизвестный код операции: {opcode}")

        instruction_pointer += 2

    return ",".join(map(str, output))


def chronospatial_computer(filename):
    """Чтение данных и эмуляция программы."""
    registers, program = parse_input(filename)
    result = emulate_3bit_computer(registers, program)
    print(f"Результат выполнения программы: {result}")
    return result


if __name__ == "__main__":
    chronospatial_computer("_input.txt")
    chronospatial_computer("input.txt")
