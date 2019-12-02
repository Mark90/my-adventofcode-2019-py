def algorithm(values, replace1, replace2):
    """Evaluate instructions until opcode at position 0 is 99.

    Args:
        values (list of int): values with instructions
        replace1 (int): replace value at position 1 with this
        replace2 (int): replace value at position 2 with this

    Returns:
        int: final value of position 0
    """
    values[1], values[2] = replace1, replace2
    pos = 0
    while True:
        op = values[pos]
        if op == 99:
            return values[0]
        inputs = values[values[pos + 1]], values[values[pos + 2]]
        values[values[pos + 3]] = (inputs[0] * inputs[1]) if op == 2 else (inputs[0] + inputs[1])
        pos += 4


def part1(lines):
    values = list(map(int, lines[0].split(",")))
    print("[part1] Index 0 is:", algorithm(values, 12, 2))


def part2(lines):
    values = list(map(int, lines[0].split(",")))

    target_output = 19690720

    base_input1, base_input2 = 0, 0
    base_output = algorithm(values.copy(), base_input1, base_input2)
    total_delta = target_output - base_output

    delta_input1 = algorithm(values.copy(), base_input1 + 1, base_input2) - base_output
    delta_input2 = algorithm(values.copy(), base_input1, base_input2 + 1) - base_output

    mult_delta1 = total_delta // delta_input1
    mult_delta2 = int((total_delta % delta_input1) / delta_input2)

    noun = base_input1 + mult_delta1
    verb = base_input2 + mult_delta2
    assert algorithm(values.copy(), noun, verb) == target_output
    print("[part2] 100 * noun + verb =", 100 * noun + verb)
