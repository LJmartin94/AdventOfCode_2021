def find_winning_board(numbers_drawn, all_boards):
    print(numbers_drawn)
    print(all_boards)
    return (0)


def main():
    file = open("input.txt")

    # Get drawn numbers
    numbers_drawn = file.readline()
    file.readline()

    # Make Bingo boards
    bingo_board = [[] for x in range(6)]
    all_boards = [bingo_board for y in range(100)]

    b = 0
    l = 0
    for line in file:
        all_boards[b][l] = line.split()
        l += 1
        l = l % 6
        if l == 0:
            b += 1

    # Find winning board & score
    winning_score = find_winning_board(numbers_drawn, all_boards)

    print("Answer to 4.0:")
    print(winning_score)


if __name__ == "__main__":
    main()