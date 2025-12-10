# Part 1 Find the largest possible "joltage" (2 digit number) for each battery bank

input = open("input.txt").read().splitlines()

joltages = []
for line in input:
   digits = []
   for c in line:
       digits.append(int(c))
   
   tens = -1
   ones = 0
   for d in range(len(digits)):
       if digits[d] > tens and d != len(digits)-1:
           tens = digits[d]
           tens_index = d

   for d in range(len(digits)):
       if d > tens_index:
           if digits[d] > ones:
               ones = digits[d]
   print("Tens place joltage in line:", tens)
   print("Ones place joltage in line:", ones)

   joltages.append(tens * 10 + ones)

sum_joltages = sum(joltages)
print("Sum of joltages:", sum_joltages)

# Part 2 Find the largest possible "joltage" made up of 12 digits
joltages = []

for line in input:
    digits = []
    for c in line.strip(): # Added .strip() just in case of newlines
        digits.append(int(c))

    last_index = -1
    result_digits = []
    
    # Loop 12 times to find 12 digits
    for i in range(12): 

        max_digit = -1
        best_index_found = -1

        digits_needed = 11 - i 
        
        search_end = len(digits) - digits_needed

        for j in range(last_index + 1, search_end):
            if digits[j] == 9:
                max_digit = 9
                best_index_found = j
                break
            elif digits[j] > max_digit:
                max_digit = digits[j]
                best_index_found = j
            
        if best_index_found != -1:
            result_digits.append(max_digit)
            last_index = best_index_found
    
    joltages.append(result_digits)

total_sum = 0
for jolt in joltages:
    jolt_string = "".join(str(j) for j in jolt)
    print(jolt_string)

    number = int(jolt_string)

    total_sum += number

print("Total sum of joltages:", total_sum)