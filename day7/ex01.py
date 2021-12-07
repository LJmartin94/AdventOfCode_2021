import statistics

def calc_incremental_fuel_cost(median, entry):
    increments = abs(median - entry)
    step_cost = 1
    total_cost = 0
    for _ in range(int(increments)):
        total_cost = total_cost + step_cost
        step_cost += 1
    return total_cost


def shift_median_for_optimal_fuel_cost(crab_list, median, direction, value_median, value_new):
    if (direction == 1):
        print("Moving median right")
    else:
        print("Moving median left")
    while value_new <= value_median:
        median = median + direction
        fuel_cost = 0
        for entry in crab_list:
            fuel_cost += calc_incremental_fuel_cost(median, entry)
        value_median = value_new
        value_new = fuel_cost
    print("New optimal point found: " + str(median - direction))
    return(value_median)

def main():
    file = open("input.txt")
    crab_list = file.readline()
    crab_list = crab_list .split(',')
    for i in range(len(crab_list)):
        crab_list[i] = int(crab_list[i])
    crab_list.sort()

    median = statistics.median(crab_list)
    print("Found initial Median: " + str(median))
    fuel_cost = 0
    for entry in crab_list:
        fuel_cost += calc_incremental_fuel_cost(median, entry)

    # Find whether there are cheaper options to the left or right of the median
    fuel_cost_right = 0
    for entry in crab_list:
        fuel_cost_right += calc_incremental_fuel_cost(median + 1, entry)
    fuel_cost_left = 0
    for entry in crab_list:
        fuel_cost_left = calc_incremental_fuel_cost(median - 1, entry)

    # If cheaper options are available, shift the optimal fuel cost point from the median in that direction,
    # until the fuel cost stops decreasing.
    if fuel_cost_right < fuel_cost:
        fuel_cost = shift_median_for_optimal_fuel_cost(crab_list, median, 1, fuel_cost, fuel_cost_right)
    else:
        if fuel_cost_left < fuel_cost:
            fuel_cost = shift_median_for_optimal_fuel_cost(crab_list, median, -1, fuel_cost, fuel_cost_left)

    answer = fuel_cost
    print("Answer to 7.1:")
    print(answer)


if __name__ == "__main__":
    main()