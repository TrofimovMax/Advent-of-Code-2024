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

def emulate_3bit_computer(registers, program, verbose=False):
    """
    Эмулирует работу 3-битного компьютера.

    :param registers: Словарь начальных значений регистров {'A': int, 'B': int, 'C': int}.
    :param program: Список инструкций программы (список чисел).
    :param verbose: Если True, выводит пошаговое выполнение.
    :return: Результат вывода программы (список чисел).
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

        if verbose:
            print(f"IP: {instruction_pointer}, Opcode: {opcode}, Operand: {operand}, Registers: A={A}, B={B}, C={C}")

        if opcode == 0:  # adv
            if get_combo_value(operand) != 0:  # Avoid division by zero
                A //= 2 ** get_combo_value(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                if verbose:
                    print(f"Jumping to {instruction_pointer}")
                continue
        elif opcode == 4:  # bxc
            B ^= C  # Операнд игнорируется
        elif opcode == 5:  # out
            output_value = get_combo_value(operand) % 8
            output.append(output_value)
            if verbose:
                print(f"Output: {output_value}")
        elif opcode == 6:  # bdv
            if get_combo_value(operand) != 0:  # Avoid division by zero
                B = A // (2 ** get_combo_value(operand))
        elif opcode == 7:  # cdv
            if get_combo_value(operand) != 0:  # Avoid division by zero
                C = A // (2 ** get_combo_value(operand))
        else:
            raise ValueError(f"Неизвестный код операции: {opcode}")

        instruction_pointer += 2

    return output

def calculate_a_for_output(program):
    """Вычисляет значение A для самовоспроизводящейся программы."""
    operand_adv = None
    for idx in range(0, len(program), 2):
        if program[idx] == 0:  # adv команда
            operand_adv = program[idx + 1]
            break

    if operand_adv is None:
        raise ValueError("Программа не содержит команду adv для восстановления A.")

    A = 0
    for output in reversed(program):
        A = (A * (2 ** operand_adv)) + output

    print(f"Восстановленное значение A: {A}")
    return A

def chronospatial_computer(filename):
    """Чтение данных, поиск минимального A и эмуляция программы."""
    registers, program = parse_input(filename)
    print("Начальные значения регистров и программа:")
    print(registers)
    print(program)

    min_a = calculate_a_for_output(program)
    registers['A'] = min_a

    output = emulate_3bit_computer(registers, program, verbose=True)
    print("Результат выполнения программы:", output)

    if output == program:
        print(f"Наименьшее значение A: {min_a}")
    else:
        print("Ошибка: восстановленное значение A не даёт правильный результат.")

    return min_a

if __name__ == "__main__":
    chronospatial_computer("__input.txt")
