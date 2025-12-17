import pprint

# Part 1 Find "fresh" ids
input = open("input.txt").read()

ranges_raw, ids_raw = input.strip().split("\n\n")

ranges = []
for line in ranges_raw.splitlines():
    start, end = line.split("-")
    ranges.append((int(start), int(end)))

ids = [] 
for line in ids_raw.splitlines():
    ids.append(int(line))

fresh_ids = set()
for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            fresh_ids.add(id)
    
print(len(fresh_ids))

# Part 2 find the number of ids considered to be fresh
sorted_ranges = sorted(ranges)

merged_ranges = []

current_start, current_end = sorted_ranges[0]
for start, end in sorted_ranges[1:]:
    if current_end >= start:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end
merged_ranges.append((current_start, current_end))

num_ids = 0
for start, end in merged_ranges:
    num_ids += (end  - start) + 1

print(num_ids)