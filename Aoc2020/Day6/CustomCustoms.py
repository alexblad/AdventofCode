## Part 1 Find the sum of question counts
answers = (x.replace('\n', ' ') for x in open("input.txt").read().split('\n\n'))

all_yeses = [set(answer.replace(' ', '')) for answer in answers]

total_yes_count = sum(len(yeses) for yeses in all_yeses)
print(total_yes_count)

## Part 2 Find the sum of unanimous question counts
answers = open("input.txt").read().split('\n\n')
unanimous_yeses = [
    set.intersection(*[set(person) for person in answer.split() if person])
    for answer in answers
]

total_unanimous_yes_count = sum(len(yeses) for yeses in unanimous_yeses)
print(total_unanimous_yes_count)