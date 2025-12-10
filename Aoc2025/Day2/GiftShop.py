import math as m
import time

# Day 2 Find invalid ids in the gift shop database

# Part 1 
input = open("input.txt").read().split(',')
ranges = []
for i in range(len(input)):
    first_id, last_id = input[i].split('-')
    ranges.append((int(first_id), int(last_id)))

#print(ranges)

invalid_ids = []

for r in ranges:
    # Iterate through each number in the range
    for id in range(r[0], r[1] + 1):
        # Get number of digits
        d = int(m.log10(id)) + 1
        
        # Check if number of digits is even
        if d % 2 != 0:
            continue

        k = d // 2
        # Calculate magic number
        m_number = 10 ** k + 1

        if id % m_number == 0:
            invalid_ids.append(id)
            #print("Invalid ID found:", id)

total_of_invalid_ids = sum(invalid_ids)

#print ("Invalid IDs:", invalid_ids)

#print("Total of invalid IDs:", total_of_invalid_ids)

# Part 2 (Continuing the mathematical approach)
invalid_ids2 = []

for r in ranges:
    for id in range(r[0], r[1] +1):
        # Get number of digits
        d = int(m.log10(id) + 1)
        
        # Find divisors of d
        divisors = []
        for i in range(1, (d//2) + 1):
            if d % i == 0:
                divisors.append(i)
        
        for l in divisors:
            mask = (10 ** d - 1) // (10 ** l - 1)
            if id % mask == 0:
                invalid_ids2.append(id)
                #print("Invalid ID found (Part 2):", id)
                break

total_of_invalid_ids2 = sum(invalid_ids2)
#print("Total of invalid IDs (Part 2):", total_of_invalid_ids2)

# Part 2 alternative: "String Doubling" method
invalid_ids3 = []
for r in ranges:
    for id in range(r[0], r[1] + 1):
        id_str = str(id)
        double_str = id_str + id_str
        search_str = double_str[1:-1]
        if id_str in search_str:
            invalid_ids3.append(id)
            #print("Invalid ID found (String Doubling):", id)
        
total_of_invalid_ids3 = sum(invalid_ids3)
#print("Total of invalid IDs (String Doubling):", total_of_invalid_ids3)

