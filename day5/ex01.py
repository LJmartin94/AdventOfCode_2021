def draw_horizontal_lines(grid, op_array):
    for op in op_array:
        xa = int(op[0][0])
        xb = int(op[1][0])
        ya = int(op[0][1])
        yb = int(op[1][1])
        if xa == xb:
            if ya > yb:
                swap = ya
                ya = yb
                yb = swap
            for i in range(yb - ya + 1):
                grid[xa][ya + i] += 1
    return grid


def draw_vertical_lines(grid, op_array):
    for op in op_array:
        xa = int(op[0][0])
        xb = int(op[1][0])
        ya = int(op[0][1])
        yb = int(op[1][1])
        if ya == yb:
            if xa > xb:
                swap = xa
                xa = xb
                xb = swap
            for i in range(xb - xa + 1):
                grid[xa + i][ya] += 1
    return grid


def draw_straight_lines(grid, op_array):
    grid = draw_horizontal_lines(grid, op_array)
    grid = draw_vertical_lines(grid, op_array)
    return grid


def is_45_diagonal(xa, xb, ya, yb):
    xdif = (xa - xb)
    ydif = (ya - yb)
    xdif *= xdif
    ydif *= ydif
    if xdif == ydif:
        return 1
    else:
        return 0


def draw_diagonal_lines(grid, op_array):
    for op in op_array:
        xa = int(op[0][0])
        xb = int(op[1][0])
        ya = int(op[0][1])
        yb = int(op[1][1])
        if is_45_diagonal(xa, xb, ya, yb) == 1:
            # Make sure coord xa,ya describes left most point of diagonal line
            if xa > xb:
                swap = xa
                xa = xb
                xb = swap
                swap = ya
                ya = yb
                yb = swap
            # Check if point a to b is a downward slope from left to right, or upward
            if ya > yb:
                ymod = -1
            else:
                ymod = 1
            for i in range(xb - xa + 1):
                grid[xa + i][ya + (i * ymod)] += 1
    return grid


def main():
    file = open("input.txt")
    line = [0 for x in range(1000)]
    grid = [line.copy() for x in range(1000)]
    op_array = []
    file_length = 500
    intersections = 0

    for i in range(file_length):
        op = file.readline().split('\n')
        op = op[0]
        op = op.split(' -> ')
        op[0] = op[0].split(',')
        op[1] = op[1].split(',')
        op_array.append(op)

    grid = draw_straight_lines(grid, op_array)
    grid = draw_diagonal_lines(grid, op_array)
    for y in range(1000):
        for x in range(1000):
            if grid[x][y] >= 2:
                intersections += 1
    # for entry in op_array:
    #     print(entry)
    for row in grid:
        print(row)

    print("Answer to 5.1:")
    print(intersections)


if __name__ == "__main__":
    main()