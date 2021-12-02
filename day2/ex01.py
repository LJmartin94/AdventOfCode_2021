
def main():
    horizontal = 0
    depth = 0
    aim = 0
    file = open("input.txt")
    for line in file:
        if line[0] == 'f':
            horizontal = horizontal + int(line[8])
            depth = depth + (aim * int(line[8]))
        if line[0] == 'd':
            aim = aim + int(line[5])
        if line[0] == 'u':
            aim = aim - int(line[3])
    print("Answer to ex01:")
    print(horizontal * depth)


if __name__ == "__main__":
    main()