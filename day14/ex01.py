from collections import Counter


def single_step(polymer, rules):
    i = 0
    while i < (len(polymer) - 1):
        for rule in rules:
            if polymer[i] == rule[0] and polymer[i + 1] == rule[1]:
                i += 1
                polymer = polymer[:i] + rule[6] + polymer[i:]
                break
        i += 1
    return polymer


def insertion_process(polymer, rules, steps):
    polymer = single_step(polymer, rules)
    if steps > 1:
        polymer = extended_insertion_process(polymer, rules, (steps - 1))
    return polymer


def extended_insertion_process(polymer, rules, steps):
    # if (steps >= 5):
    #     print("steps to go: " + str(steps))
    segments = len(polymer) - 1
    polymer_segments = []
    polymer_solved = []
    for s in range(segments):
        polymer_segments.append(str(polymer[s] + polymer[s+1]))
        polymer_solved.append(insertion_process(polymer_segments[s], rules, steps))
        # print(polymer_solved)
    for s in range(len(polymer_solved)):
        if s > 0:
            polymer_solved[s] = polymer_solved[s][1:]
    polymer = ''.join(polymer_solved)
    # print(polymer)
    return polymer


def main():
    lines = open("test_input.txt").read().split('\n')
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
    polymer = extended_insertion_process(polymer, rules, steps)
    elements = Counter(polymer)
    elements = elements.most_common(len(elements))
    most_common = elements[0][1]
    least_common = elements[len(elements) - 1][1]
    answer = most_common - least_common
    print("Answer to 14.1:")
    print(answer)


if __name__ == "__main__":
    main()