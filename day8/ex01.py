from enum import IntEnum


class TotalSegments(IntEnum):
    # Unique:
    ONE = 2  # TOP_RIGHT, BOTTOM_RIGHT
    FOUR = 4  # TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT
    SEVEN = 3  # TOP, TOP_RIGHT, BOTTOM_RIGHT
    EIGHT = 7  # TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM

    # Doesn't contain: Middle (in 4/8, not in 1/7)
    ZERO = 6  # TOP, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
    # Doesn't contain: Top Right (in 1/4/7/8)
    SIX = 6  # TOP, TOP_LEFT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
    # Doesn't contain: Bottom Left (in 8, not in 1/4/7)
    NINE = 6  # TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT, BOTTOM

    # One: 1seg Four: 2seg
    TWO = 5  # TOP, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM
    THREE = 5  # TOP, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT, BOTTOM
    FIVE = 5  # TOP, TOP_LEFT, MIDDLE, BOTTOM_RIGHT, BOTTOM


class SegPos(IntEnum):
    TOP = 0
    TOP_LEFT = 1
    TOP_RIGHT = 2
    MIDDLE = 3
    BOTTOM_LEFT = 4
    BOTTOM_RIGHT = 5
    BOTTOM = 6


def decypher_one(line_key, digit):
    # filter line key for every entry,
    # checking if the entry can be found in the list of characters the digit specifies or not
    line_key[SegPos.TOP] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    line_key[SegPos.TOP_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    # line_key[SegPos.TOP_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP]))
    line_key[SegPos.MIDDLE] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    line_key[SegPos.BOTTOM_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    # line_key[SegPos.BOTTOM_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP]))
    line_key[SegPos.BOTTOM] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    return line_key


def main():
    file = open("test_input.txt")
    output_vals = []

    for line in file:
        output_line = line.split(' | ')[1].split('\n')[0].split()
        output_vals.append(output_line)

    decoded_lines = []
    possible_segments = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for line in output_vals:
        i = 0
        decoded_line = ['x' for _ in range(4)]
        line_key = [possible_segments.copy() for _ in range(7)]
        for digit in line:
            if len(digit) == TotalSegments.ONE:
                decoded_line[i] = 1
                line_key = decypher_one(line_key, digit)
                print(line_key)
            if len(digit) == TotalSegments.FOUR:
                decoded_line[i] = 4
            if len(digit) == TotalSegments.SEVEN:
                decoded_line[i] = 7
            if len(digit) == TotalSegments.EIGHT:
                decoded_line[i] = 8
            if len(digit) == TotalSegments.TWO:
                decoded_line[i] = '235 ' + digit
            if len(digit) == TotalSegments.ZERO:
                decoded_line[i] = '069 ' + digit
            i += 1
        # print (line_key)
        decoded_lines.append(decoded_line)

    answer = decoded_lines
    print("Answer to 8.1:")
    print(answer)



if __name__ == "__main__":
    main()
