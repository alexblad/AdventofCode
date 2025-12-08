# Part 1 Find the number of times the dial lands on 0
input = open("input.txt").read().splitlines()

zeros = 0

dial_positions = [i for i in range (100)]

# print(dial_positions)
dial = 50

for line in input:
    direction, distance = line[0], int(line[1:])
    if distance > 100:
        distance = distance % 100
    if direction == "L":
        dial = dial_positions[(dial - distance)%100]
        #print(dial)
    if direction == "R":
        dial = dial_positions[(dial + distance)%100]
        #print(dial)
    if dial_positions[dial] == 0:
        zeros += 1

print(zeros)

# Part 2 Find the number of times the dials lands on or passes 0
zeros = 0
dial = 50

for line in input:
    direction, distance = line[0], int(line[1:])
    for num in range (distance):
        if direction == "L":
            dial = dial_positions[(dial - 1)%100]
        if direction == "R":
            dial = dial_positions[(dial + 1)%100]
        if dial_positions[dial] == 0:
            zeros += 1

print(zeros)