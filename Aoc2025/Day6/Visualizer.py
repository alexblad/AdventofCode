import time

def print_section(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

# Read input
print_section("STEP 1: READING INPUT")
input_data = open("input.txt").read().splitlines()
for i, line in enumerate(input_data):
    print(f"Line {i}: '{line}'")

# Pad lines
print_section("STEP 2: PADDING LINES")
max_len = max(len(line) for line in input_data)
print(f"Max line length found: {max_len}")
padded_lines = [line.ljust(max_len) for line in input_data]

print("Padded lines (dots '.' represent spaces added):")
for i, line in enumerate(padded_lines):
    # Visualize spaces as dots for clarity
    visual_line = line.replace(' ', '.')
    print(f"Line {i}: '{visual_line}'")

# Transpose
print_section("STEP 3: TRANSPOSING (The Geometric Twist)")
print("Rotating the grid so columns become rows...")
columns = list(zip(*padded_lines))

print(f"Resulting 'columns' (now rows in our list):")
for i, col in enumerate(columns):
    # Join tuple to string for display
    col_str = "".join(col)
    visual_col = col_str.replace(' ', '.')
    print(f"Col {i}: '{visual_col}'")

# Grouping
print_section("STEP 4: GROUPING PROBLEMS")
problems = []
current_problem = []
problem_count = 0

for i, col in enumerate(columns):
    is_separator = all(c == ' ' for c in col)
    
    if is_separator:
        status = "SEPARATOR (All spaces)"
        if current_problem:
            problems.append(current_problem)
            print(f"  -> Finished Problem #{len(problems)}")
            current_problem = []
    else:
        status = "DATA COLUMN"
        current_problem.append(col)
    
    # Show a few examples or all if small
    print(f"Processing Col {i}: {status}")

if current_problem:
    problems.append(current_problem)
    print(f"  -> Finished Problem #{len(problems)}")

# Solving
print_section("STEP 5: SOLVING EACH PROBLEM")
part2_total = 0

for i, problem in enumerate(problems):
    print(f"\n--- Solving Problem #{i+1} ---")
    numbers = []
    operator = None
    
    print("  Raw columns in this problem:")
    for col in problem:
        print(f"    {col}")

    print("\n  Parsing columns:")
    for col in problem:
        # The symbol at the bottom (last element) is the operator
        char_at_bottom = col[-1]
        
        if char_at_bottom in ('+', '*'):
            operator = char_at_bottom
            print(f"    Found Operator at bottom: '{operator}'")
        
        # The rest of the column is the number
        raw_num_chars = col[:-1]
        num_str = "".join(raw_num_chars).replace(" ", "")
        
        if num_str:
            number = int(num_str)
            print(f"    Parsed Number: {number} (from '{''.join(raw_num_chars)}')")
            numbers.append(number)
        else:
             print(f"    (Empty number column, skipping)")

    result = 0
    if operator == '+':
        result = sum(numbers)
        print(f"  Calculation: Sum({numbers}) = {result}")
        part2_total += result
    elif operator == '*':
        product = 1
        for num in numbers:
            product *= num
        result = product
        print(f"  Calculation: Product({numbers}) = {result}")
        part2_total += result
    else:
        print(f"  WARNING: No operator found!")

print_section("FINAL RESULT")
print(f"Total Sum: {part2_total}")
