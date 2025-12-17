# Part 1
input = open("input.txt").read().splitlines()

line_1 = [int(x) for x in input[0].split()]
line_2 = [int(x) for x in input[1].split()]
line_3 = [int(x) for x in input[2].split()]
line_4 = [int(x) for x in input[3].split()]
line_5 = input[4].split()

results =[]
for n1, n2, n3, n4, symbol in zip(line_1, line_2, line_3, line_4, line_5):
    if symbol == "+":
        sum_loop = n1 + n2 + n3 + n4
        results.append(sum_loop)
    if symbol == "*":
        product_loop = n1 * n2 * n3 * n4
        results.append(product_loop)

total = sum(results)
print(total)

# Part 2 Cephalapod boogaloo

# Pad lines to the same length to form a proper grid
max_len = max(len(line) for line in input)
padded_lines = [line.ljust(max_len) for line in input]

# Transpose the grid: columns become rows
# This allows us to iterate over "columns" of the original input easily
columns = list(zip(*padded_lines))

problems = []
current_problem = []

for col in columns:
    # If a column is all spaces, it's a separator between problems
    if all(c == ' ' for c in col):
        if current_problem:
            problems.append(current_problem)
            current_problem = []
    else:
        current_problem.append(col)

# Add the last problem if it exists
if current_problem:
    problems.append(current_problem)

part2_total = 0

for problem in problems:
    numbers = []
    operator = None
    
    for col in problem:
        # The symbol at the bottom (last element) is the operator
        if col[-1] in ('+', '*'):
            operator = col[-1]
        
        # The rest of the column is the number (MSD at top)
        # Join the characters and strip spaces
        num_str = "".join(col[:-1]).replace(" ", "")
        if num_str:
            numbers.append(int(num_str))

    if operator == '+':
        part2_total += sum(numbers)
    elif operator == '*':
        product = 1
        for num in numbers:
            product *= num
        part2_total += product
    
print(part2_total)


line_1 = input[0]
line_2 = input[1]

print(len(line_1), len(line_2))