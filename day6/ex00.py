def main():
    file = open("input.txt")
    simulation = file.readline()
    simulation = simulation.split(',')
    simulation.sort()
    days_to_run = 256

    # Make an array to store the number of fish per 'timer'
    schools = [0 for _ in range(9)]

    # Count how many of each fish there are
    for entry in simulation:
        schools[int(entry)] += 1

    # Variable for days passed
    passed = 0

    # Per day, move every counter down one, and set 0s to 6,
    # but also add an equal number of 8s.
    # (you can overwrite the number at index 8, because they all became 7)
    for day in range(days_to_run):
        passed += 1
        number_of_zeros = schools[0]
        for i in range(8):
            schools[i] = schools[i + 1]
        schools[6] += number_of_zeros
        schools[8] = number_of_zeros
        print(passed)
        print(schools)

    # For the final answer, sum up how many of each fish there are
    answer = sum(schools)
    print("Answer to 6.0 & 6.1:")
    print(answer)


if __name__ == "__main__":
    main()