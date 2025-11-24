## Part 1 Find accumulator value before infinite loop
input = open("input.txt").read().splitlines()

def execute_instructions(input):
    accumulator = 0
    instructions = []
    for line in input:
        operation, argument = line.split()
        instructions.append([operation, int(argument)])

    executed_instructions = set()

    i = 0
    while i < len(instructions):
        if i not in executed_instructions:
            if instructions[i][0] == "acc":
                accumulator += instructions[i][1]
            elif instructions[i][0] == "jmp":
                i += instructions[i][1] - 1
            executed_instructions.add(i)
            i += 1
        else:
            break
    return accumulator

print(execute_instructions(input))





