# Today's challenge:
# Make the program as fast as possible

program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,57,23,224,101,-1311,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,57,67,225,102,67,150,224,1001,224,-2613,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,179,213,224,1001,224,-469,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1001,188,27,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,1,184,218,224,1001,224,-155,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,21,80,224,1001,224,-101,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,67,39,225,1101,89,68,225,101,69,35,224,1001,224,-126,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,7,52,225,1102,18,90,225,1101,65,92,225,1002,153,78,224,101,-6942,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,67,83,225,1102,31,65,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,108,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,359,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,434,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1008,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226]

opcode_block_sizes = [
    1, # Opcode 0 doesnt exist
    4, # Opcode 1: add
    4, # Opcode 2: multiply
    2, # Opcode 3: input
    2 # Opcode 4: output
]


def solve_opcode(opcode_string):
    if len(opcode_string) <= 2:
        return (int(opcode_string), 0, 0, 0)
    else:
        opcode = int(opcode_string[-2:])
        opcode_string = opcode_string.rjust(5).replace(' ', '0')

        m1 = int(opcode_string[0])
        m2 = int(opcode_string[1])
        m3 = int(opcode_string[2])

        return (opcode, m3, m2, m1)


def get_value_with_mode(parameter, mode):
    global program

    value = 0
    if mode == 0: # Position mode
        value = program[parameter]
    elif mode == 1: # Immediate mode(write instruction will never be in this mode)
        value = parameter

    return value


def process(opcode, parameters, modes):
    global program

    value = 0
    if opcode == 1:
        value = get_value_with_mode(parameters[0], modes[0]) + get_value_with_mode(parameters[1], modes[1])
        program[parameters[2]] = value
    elif opcode == 2:
        value = get_value_with_mode(parameters[0], modes[0]) * get_value_with_mode(parameters[1], modes[1])
        program[parameters[2]] = value
    elif opcode == 3:
        try:
            value = int(input('Enter a number > '))
            program[parameters[0]] = value
        except:
            process(opcode, parameters)
    elif opcode == 4:
        value = program[parameters[0]]
        print(f'Output: {value}')

    global current_total_index
    current_total_index += opcode_block_sizes[opcode]

    return value

current_total_index = 0

while program[current_total_index] != 99:
    opcode_string = str(program[current_total_index])
    opcode, c, b, a = solve_opcode(opcode_string)

    if opcode == 0:
        continue

    parameters = []

    for i in range(opcode_block_sizes[opcode] - 1):
        parameters.append(program[current_total_index + (i+1)])
    process(opcode, parameters, [c, b, a])

print('Program finished with opcode 99')
print(program)
