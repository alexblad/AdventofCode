input = open("input.txt").read().strip().split('\n')
print(input)

myBagColor = "shiny gold"
bagRules = {}

for line in input:
    outerBag, innerBags = line.split(" bags contain ")
    innerBagList = innerBags.split(", ")
    bagRules[outerBag] = []
    for bag in innerBagList:
        if bag == "no other bags.":
            continue
        bagParts = bag.split(" ")
        count = int(bagParts[0])
        color = " ".join(bagParts[1:3])
        bagRules[outerBag].append((count, color))

def canContain(bagColor, targetColor):
    if bagColor not in bagRules:
        return False
    for count, innerColor in bagRules[bagColor]:
        if innerColor == targetColor or canContain(innerColor, targetColor):
            return True
    return False

# Part 1: Count how many bag colors can eventually contain at least one shiny gold bag
count = 0
for bagColor in bagRules:
    if canContain(bagColor, myBagColor):
        count += 1

print(count)

# Part 2: Count how many individual bags are required inside a single shiny gold bag
def countBags(bagColor):
    if bagColor not in bagRules:
        return 0
    total = 0
    for count, innerColor in bagRules[bagColor]:
        total += count * (1 + countBags(innerColor))
    return total

print(countBags(myBagColor))