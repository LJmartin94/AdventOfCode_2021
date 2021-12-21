from collections import Counter


def insertion_process(polymer, rules, steps):
    for _ in range(steps):
        i = 0
        while i < (len(polymer) - 1):
            for rule in rules:
                if polymer[i] == rule[0] and polymer[i+1] == rule[1]:
                    i += 1
                    polymer = polymer[:i] + rule[6] + polymer[i:]
                    break
            i += 1
        print(i + 1)
    return polymer


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

    steps = 10
    polymer = insertion_process(polymer, rules, steps)
    elements = Counter(polymer)
    elements = elements.most_common(len(elements))
    most_common = elements[0][1]
    least_common = elements[len(elements) - 1][1]
    answer = most_common - least_common
    print("Answer to 14.0:")
    print(answer)


if __name__ == "__main__":
    main()