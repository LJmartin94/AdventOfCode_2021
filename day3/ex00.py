def main():
    gamma = [0 for _ in range(12)]
    gamma_num = 0
    epsilon = [0 for _ in range(12)]
    epsilon_num = 0

    file = open("input.txt")
    for line in file:
        i = 0
        for i in range(12):
            if line[i] == '1':
                gamma[i] += 1
            if line[i] == '0':
                gamma[i] -= 1

    for i in range(12):
        if gamma[i] < 0:
            gamma[i] = 0
        if gamma[i] > 0:
            gamma[i] = 1

    bit = 2048
    for i in range(12):
        if gamma[i] == 1:
            gamma_num += bit
        else:
            epsilon_num += bit
        bit = bit / 2

    power = gamma_num * epsilon_num
    print("Answer to 3.0:")
    print(power)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()