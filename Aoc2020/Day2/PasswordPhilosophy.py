## Part 1: Find how many passwords are valid
passwords = [x.strip() for x in open("input.txt").readlines()]

validPass = 0

for password in passwords:
    policy, pw = password.split(": ")
    limits, letter = policy.split(" ")
    minLimit, maxLimit = limits.split("-")
    minLimit = int(minLimit)
    maxLimit = int(maxLimit)

    letterCount = pw.count(letter)

    if letterCount >= minLimit and letterCount <= maxLimit:
        validPass += 1

print(validPass)

## Part 2: Find how many passwords are valid according to the new interpretation
validPass = 0

for password in passwords:
    policy, pw = password.split(": ")
    positions, letter = policy.split(" ")
    pos1, pos2 = positions.split("-")
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1

    firstPosMatch = pw[pos1] == letter
    secondPosMatch = pw[pos2] == letter

    if firstPosMatch != secondPosMatch:
        validPass += 1

print(validPass)