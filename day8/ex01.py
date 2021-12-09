from enum import IntEnum


class TotalSegments(IntEnum):
    # Unique:
    ONE = 2  # TOP_RIGHT, BOTTOM_RIGHT
    FOUR = 4  # TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT
    SEVEN = 3  # TOP, TOP_RIGHT, BOTTOM_RIGHT
    EIGHT = 7  # TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM

    # Doesn't contain: Middle
    ZERO = 6  # TOP, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
    # Doesn't contain: Top Right
    SIX = 6  # TOP, TOP_LEFT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
    # Doesn't contain: Bottom Left
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

# The following functions rule out what segments can correspond to what for the 'easy' digits (1478)
def decypher_one(line_key, digit):
    # filter line key for every entry,
    # checking if the entry can be found in the list of characters the digit specifies or not
    line_key[SegPos.TOP] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    line_key[SegPos.TOP_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP_LEFT]))
    line_key[SegPos.TOP_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP_RIGHT]))
    line_key[SegPos.MIDDLE] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.MIDDLE]))
    line_key[SegPos.BOTTOM_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM_LEFT]))
    line_key[SegPos.BOTTOM_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.BOTTOM_RIGHT]))
    line_key[SegPos.BOTTOM] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM]))
    return line_key


def decypher_four(line_key, digit):
    # filter line key for every entry,
    # checking if the entry can be found in the list of characters the digit specifies or not
    line_key[SegPos.TOP] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP]))
    line_key[SegPos.TOP_LEFT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP_LEFT]))
    line_key[SegPos.TOP_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP_RIGHT]))
    line_key[SegPos.MIDDLE] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.MIDDLE]))
    line_key[SegPos.BOTTOM_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM_LEFT]))
    line_key[SegPos.BOTTOM_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.BOTTOM_RIGHT]))
    line_key[SegPos.BOTTOM] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM]))
    return line_key


def decypher_seven(line_key, digit):
    # filter line key for every entry,
    # checking if the entry can be found in the list of characters the digit specifies or not
    line_key[SegPos.TOP] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP]))
    line_key[SegPos.TOP_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.TOP_LEFT]))
    line_key[SegPos.TOP_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.TOP_RIGHT]))
    line_key[SegPos.MIDDLE] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.MIDDLE]))
    line_key[SegPos.BOTTOM_LEFT] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM_LEFT]))
    line_key[SegPos.BOTTOM_RIGHT] = list(filter(lambda entry: digit.find(entry) != -1, line_key[SegPos.BOTTOM_RIGHT]))
    line_key[SegPos.BOTTOM] = list(filter(lambda entry: digit.find(entry) == -1, line_key[SegPos.BOTTOM]))
    return line_key


# The following function decyphers 6 segment digits:
# (Each six-segment digit is missing exactly one segment of the 7 total,
# and each segment can only be one of at most two letters by the time 1478 have been decyphered;
# if a digit is missing either letter possibility, it is missing that segment)
def decypher_six_seg(digit, line_key):
    mida = line_key[SegPos.MIDDLE][0]
    midb = line_key[SegPos.MIDDLE][1]
    topra = line_key[SegPos.TOP_RIGHT][0]
    toprb = line_key[SegPos.TOP_RIGHT][1]
    botla = line_key[SegPos.BOTTOM_LEFT][0]
    botlb = line_key[SegPos.BOTTOM_LEFT][1]
    digit_id = -1
    if digit.find(mida) == -1 or digit.find(midb) == -1:
        digit_id = 0
    if digit.find(topra) == -1 or digit.find(toprb) == -1:
        digit_id = 6
    if digit.find(botla) == -1 or digit.find(botlb) == -1:
        digit_id = 9
    return (digit_id)


# The following function decyphers 5 segment digits:
# (of the five segment digits, each has a unique pair;
# only 5 has both top_left AND middle
# only 3 has top right AND top left
# only 2 has bottom left AND bottom.
# By the time 1478 have been disambiguated, these pairs share the same
# letter possibilities, so if a digit has both letters they are identified
# by their unique pair)
def decypher_five_seg(digit, line_key):
    fivea = line_key[SegPos.MIDDLE][0]
    fiveb = line_key[SegPos.MIDDLE][1]
    threea = line_key[SegPos.TOP_RIGHT][0]
    threeb = line_key[SegPos.TOP_RIGHT][1]
    twoa = line_key[SegPos.BOTTOM_LEFT][0]
    twob = line_key[SegPos.BOTTOM_LEFT][1]
    digit_id = -1
    if digit.find(fivea) != -1 and digit.find(fiveb) != -1:
        digit_id = 5
    if digit.find(threea) != -1 and digit.find(threeb) != -1:
        digit_id = 3
    if digit.find(twoa) != -1 and digit.find(twob) != -1:
        digit_id = 2
    return (digit_id)


def main():
    file = open("input.txt")
    output_vals = []
    input_lines = 200

    for line in file:
        output_line = line.split('\n')[0].split()
        output_vals.append(output_line)

    decoded_lines = []
    possible_segments = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for line in output_vals:
        decoded_line = ['x' for _ in range(15)]
        line_key = [possible_segments.copy() for _ in range(7)]
        # Disambiguate obvious numbers first
        i = 0
        for digit in line:
            if len(digit) == TotalSegments.ONE:
                decoded_line[i] = 1
                line_key = decypher_one(line_key, digit)
            if len(digit) == TotalSegments.FOUR:
                decoded_line[i] = 4
                line_key = decypher_four(line_key, digit)
            if len(digit) == TotalSegments.SEVEN:
                decoded_line[i] = 7
                line_key = decypher_seven(line_key, digit)
            if len(digit) == TotalSegments.EIGHT:
                decoded_line[i] = 8
            if len(digit) == TotalSegments.TWO or len(digit) == TotalSegments.ZERO:
                decoded_line[i] = digit
            i += 1
        # Disambiguate six & five segment digits next
        i = 0
        for digit in line:
            if len(digit) == TotalSegments.SIX:  # Happily, the digit six consists of six segments
                decoded_line[i] = decypher_six_seg(digit, line_key)
            if len(digit) == TotalSegments.FIVE:  # Happily, the digit five consists of five segments
                decoded_line[i] = decypher_five_seg(digit, line_key)
            i += 1
        decoded_lines.append(decoded_line)

    for i in range(input_lines):
        final_val = decoded_lines[i][11] * 1000
        final_val += decoded_lines[i][12] * 100
        final_val += decoded_lines[i][13] * 10
        final_val += decoded_lines[i][14]
        decoded_lines[i] = final_val

    answer = sum(decoded_lines)
    print("Answer to 8.1:")
    print(answer)


if __name__ == "__main__":
    main()
