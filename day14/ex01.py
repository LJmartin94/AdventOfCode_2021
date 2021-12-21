from collections import Counter


def convert_pairs_to_letters(pairs):
    letters = []
    letters = Counter(letters)
    for p in range(len(pairs)):
        first_letter = pairs.most_common(len(pairs))[p][0][0]
        value = pairs.most_common(len(pairs))[p][1]
        letters.update({first_letter: value})
    return letters


def update_pairs(pairs, rules, steps):
    for s in range(steps):
        changes = []
        changes = Counter(changes)
        for pair in pairs:
            for rule in rules:
                if rule.find(pair) != -1:
                    insertion = rule[6]
                    old_pair = pair
                    new_pairA = str(pair[0] + insertion)
                    new_pairB = str(insertion + pair[1])
                    changes.update({new_pairA: pairs[old_pair]})
                    changes.update({new_pairB: pairs[old_pair]})
                    changes.update({old_pair: (pairs[old_pair] * -1)})
        pairs.update(changes)
    return pairs


def main():
    lines = open("input.txt").read().split('\n')
    polymer = ""
    rules = []
    breaker = 0
    for line in lines:
        if line == '':
            breaker = 1
            continue
        if breaker == 0:
            polymer = line
        if breaker == 1:
            rules.append(line)

    steps = 40
    pairs = []
    for i in range(len(polymer) - 1):
        pairs.append(str(polymer[i]) + str(polymer[i+1]))
    pairs = Counter(pairs)
    pairs = update_pairs(pairs, rules, steps)
    letters = convert_pairs_to_letters(pairs)
    last_letter = polymer[len(polymer) - 1]
    letters.update({last_letter: 1})

    elements = letters.most_common(len(letters))
    most_common = elements[0][1]
    least_common = elements[len(elements) - 1][1]
    answer = most_common - least_common
    print("Answer to 14.1:")
    print(answer)


if __name__ == "__main__":
    main()