from enum import IntEnum


class Segments(IntEnum):
    ZERO = 6
    ONE = 2
    TWO = 5
    THREE = 5
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 3
    EIGHT = 7
    NINE = 6


def main():
    file = open("input.txt")
    output_vals = []

    for line in file:
        output_line = line.split(' | ')[1].split('\n')[0].split()
        output_vals.append(output_line)

    easy_digits = 0
    for line in output_vals:
        for digit in line:
            if len(digit) == Segments.ONE or len(digit) == Segments.FOUR or \
            len(digit) == Segments.SEVEN or len(digit) == Segments.EIGHT:
                easy_digits += 1

    answer = easy_digits
    print("Answer to 8.0:")
    print(answer)


if __name__ == "__main__":
    main()