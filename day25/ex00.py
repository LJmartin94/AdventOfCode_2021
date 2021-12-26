def main():
    lines = open("test_input.txt").read().split('\n')
    dimy = len(lines)
    dimx = len(lines[0])

    map = [[0 for _ in range(dimx)] for _ in range(dimy)]
    y = 0
    for line in lines:
        x = 0
        for char in line:
            map[y][x] = char
            x += 1
        y += 1

    for row in map:
        print(row)

    answer = lines
    print("Answer to 25.0:")
    print(answer)


if __name__ == "__main__":
    main()