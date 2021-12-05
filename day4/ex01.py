g_winning_boards = []

def visualiser(current_num, all_boards):
    print("Number this turn:" + current_num)
    for board in all_boards:
        for row in board:
            print(row)
        print('\n')


def calc_winning_score(current_num, winning_board):
    unmarked_total = 0
    for y in range(5):
        for x in range(5):
            if winning_board[y][x] != 'x':
                unmarked_total += int(winning_board[y][x])
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
                if g_winning_boards.count([b]) == 0:
                    g_winning_boards.append([b])
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
                if g_winning_boards.count([b]) == 0:
                    g_winning_boards.append([b])
        b += 1
    return -1


def find_winning_board(numbers_drawn, all_boards):
    all_winning_boards = [-1]
    board_n = 0
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
        if len(g_winning_boards) == 100:
            break
    winning_board = int(g_winning_boards[99][0])
    return calc_winning_score(current_num, all_boards[winning_board])
    return 0


def main():
    file = open("input.txt")

    # Get drawn numbers
    numbers_drawn = file.readline()
    file.readline()

    # Make Bingo boards
    all_boards = []

    all_input = [[] for x in range(600)]
    for i in range(600):
        all_input[i] = file.readline().split()

    K = 6
    board = []
    row_count = 0
    for row in all_input:
        board.append(row)
        row_count += 1
        if row_count >= K:
            all_boards.append(board)
            board = []
            row_count = 0

    # Find winning board & score
    winning_score = find_winning_board(numbers_drawn, all_boards)

    print("Answer to 4.1:")
    print(winning_score)


if __name__ == "__main__":
    main()