## Part 1: Find how many tree are hit
treeMap = [x.strip() for x in open("input.txt").readlines()]

treeCount = 0
rowLength = len(treeMap[0])

x_pos = 0

for row in treeMap:
    if row[x_pos] == '#':
        treeCount += 1

    x_pos = (x_pos + 3) % rowLength

print(treeCount)

## Part 2: Find how many trees are hit for different slopes

slopes = [(1,1,), (3,1), (5,1), (7,1), (1,2)]

treeCounts = []

for slope in slopes:
    treeCount = 0
    x_pos = 0
    y_pos = 0

    while y_pos < len(treeMap):
        if treeMap[y_pos][x_pos] == '#':
            treeCount += 1

        x_pos = (x_pos + slope[0]) % rowLength
        y_pos += slope[1]

    treeCounts.append(treeCount)

product = 1
for count in treeCounts: product *= count

print(product)

