def calc_ox():
    oxygen = [0 for _ in range(12)]
    oxygen_num = 0
    left_over = [[] for _ in range(1000)]
    unique_nums = 0

    file = open("input.txt")
    i = 0
    for line in file:
        left_over[i] = line
        i += 1

    for i in range(12):
        for line in left_over:
            if line[i] == '1':
                oxygen[i] += 1
            if line[i] == '0':
                oxygen[i] -= 1
        if oxygen[i] >= 0:
            oxygen[i] = 1
        else:
            oxygen[i] = 0
        noise = "222222222222\n"
        unique_nums = 0
        for x in range(1000):
            if left_over[x][i] != str(oxygen[i]):
                left_over[x] = noise
            else:
                unique_nums += 1
        if unique_nums == 1:
            break

    for x in range(1000):
        if left_over[x][0] != '2':
            oxygen = left_over[x]

    bit = 2048
    for i in range(12):
        if oxygen[i] == '1':
            oxygen_num += bit
        bit = bit / 2
    return oxygen_num


def calc_carbdox():
    carbondioxide = [0 for _ in range(12)]
    co_num = 0
    left_over = [[] for _ in range(1000)]
    unique_nums = 0

    file = open("input.txt")
    i = 0
    for line in file:
        left_over[i] = line
        i += 1

    for i in range(12):
        for line in left_over:
            if line[i] == '1':
                carbondioxide[i] += 1
            if line[i] == '0':
                carbondioxide[i] -= 1
        if carbondioxide[i] >= 0:
            carbondioxide[i] = 0
        else:
            carbondioxide[i] = 1
        noise = "222222222222\n"
        unique_nums = 0
        for x in range(1000):
            if left_over[x][i] != str(carbondioxide[i]):
                left_over[x] = noise
            else:
                unique_nums += 1
        if unique_nums == 1:
            break

    for x in range(1000):
        if left_over[x][0] != '2':
            carbondioxide = left_over[x]

    bit = 2048
    for i in range(12):
        if carbondioxide[i] == '1':
            co_num += bit
        bit = bit / 2
    return co_num


def main():
    oxygen = calc_ox()
    carbondioxide = calc_carbdox()

    print(oxygen)
    print(carbondioxide)
    life_support = oxygen * carbondioxide
    print("Answer to 3.1:")
    print(life_support)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()