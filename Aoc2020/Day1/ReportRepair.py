## Part 1: Find the two entries that sum to 2020; and multiply then together
input = [int(x) for x in open("input.txt").readlines()]

sortedInput = sorted(input)

left = 0
right = len(sortedInput) - 1

## Walk the pointers
while (left < right):
    currentSum = sortedInput[left] + sortedInput[right]

    if (currentSum == 2020):
        print(sortedInput[left] * sortedInput[right])
        break

    elif (sortedInput[left] + sortedInput[right] < 2020):
        left += 1
    else:
        right -= 1


## Part 2: Find the three entries that sum to 2020; and multiply then together
for i in range(len(sortedInput)-2):
    left = i + 1
    right = len(sortedInput) - 1 

    while (left < right):
        sumTarget = 2020 - sortedInput[i]

        if (sortedInput[left] + sortedInput[right] == sumTarget):
            print(sortedInput[i] * sortedInput[left] * sortedInput[right])
            break

        elif (sumTarget > (sortedInput[left] + sortedInput[right])):
            left += 1
        else:
            right -= 1