def visualiser(current_num, all_boards):
    print("Number this turn:" + current_num)
    for board in all_boards:
        for row in board:
            print(row)
        print('\n')

def calc_winning_score(current_num, winning_board):
    # print("Winning board:\n" + str(winning_board))
    # print("Winning num:\n" + str(current_num))
    unmarked_total = 0
    for y in range(5):
        for x in range(5):
            if winning_board[y][x] != 'x':
                unmarked_total += int(winning_board[y][x])
    print(str(unmarked_total))
    print(str(current_num))
    score = int(unmarked_total) * int(current_num)
    return score


def check_all_boards(all_boards):
    # # check rows
    b = 0
    for board in all_boards:
        r = 0
        for row in board:
            win_score = 0
            n = 0
            for number in row:
                if number == 'x':
                    win_score += 1
                n += 1
            if win_score == 5:
                return b
            r += 1
        b += 1
    # check columns
    b = 0
    for board in all_boards:
        for x in range(5):
            win_score = 0
            for y in range(5):
                if board[y][x] == 'x':
                    win_score += 1
            if win_score == 5:
                return b
        b += 1
    return -1


def find_winning_board(numbers_drawn, all_boards):
    numbers_drawn = numbers_drawn.split(',')
    # Mark of current_num with x
    for i in range(len(numbers_drawn)):
        current_num = numbers_drawn[i]
        b = 0
        for board in all_boards:
            r = 0
            for row in board:
                n = 0
                for number in row:
                    if number == current_num:
                        all_boards[b][r][n] = 'x'
                    n += 1
                r += 1
            b += 1
        # After every number is marked off, check if any boards have won
        winning_board = check_all_boards(all_boards)
        # visualiser(current_num, all_boards)
        if winning_board != -1:
            print("Winning board index: " + str(winning_board))
            return calc_winning_score(current_num, all_boards[winning_board])
    return 0


def main():
    file = open("input.txt")

    # Get drawn numbers
    numbers_drawn = file.readline()
    file.readline()

    # Make Bingo boards
    bingo_row = [[] for x in range(5)]
    bingo_board = [bingo_row for y in range(6)]
    all_boards = [bingo_board for z in range(100)]

    all_input = [[] for x in range(600)]
    for i in range(600):
        all_input[i] = file.readline().split()

    board = 0
    line = 0
    for i in range(600):
        # print(str(board) + "," + str(line) + "  writing index: " + str(i))
        for fuckoff in range(len(all_input[i])):
            all_boards[board][line][fuckoff] = all_input[i][fuckoff]
        # print(all_boards[board][line])
        line += 1
        line = line % 6
        if line == 0:
            board += 1

    # visualiser('1', all_boards)
    print(all_boards)
    # Find winning board & score
    winning_score = find_winning_board(numbers_drawn, all_boards)

    print("Answer to 4.0:")
    print(winning_score)


if __name__ == "__main__":
    main()