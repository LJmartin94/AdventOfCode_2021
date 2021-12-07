import statistics

def main():
    file = open("test_input.txt")
    crab_list = file.readline()
    crab_list = crab_list .split(',')
    for i in range(len(crab_list)):
        crab_list[i] = int(crab_list[i])
    crab_list.sort()

    median = statistics.median(crab_list)
    print(median)
    fuel_cost = 0
    for entry in crab_list:
        fuel_cost += abs(median - entry)
    answer = fuel_cost
    print("Answer to 7.0:")
    print(answer)


if __name__ == "__main__":
    main()