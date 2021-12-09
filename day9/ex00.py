def check_lowpoint(y, x, grid, ydims, xdims):
    lowpoint = 1
    north = (y - 1, x)
    south = (y + 1, x)
    west = (y, x - 1)
    east = (y, x + 1)

    if north[0] >= 0:
        if grid[y][x] >= grid[north[0]][north[1]]:
            lowpoint = 0
    if south[0] < ydims:
        if grid[y][x] >= grid[south[0]][south[1]]:
            lowpoint = 0
    if west[1] >= 0:
        if grid[y][x] >= grid[west[0]][west[1]]:
            lowpoint = 0
    if east[1] < xdims:
        if grid[y][x] >= grid[east[0]][east[1]]:
            lowpoint = 0
    return lowpoint


def find_lowest_points(grid, ydims, xdims):
    list_lowests = []
    for y in range(ydims):
        for x in range(xdims):
            if check_lowpoint(y, x, grid, ydims, xdims) == 1:
                list_lowests.append(int(grid[y][x]))
    return list_lowests


def main():
    file = open("input.txt")
    ydims = 100
    grid = [[] for _ in range(ydims)]

    for y in range(ydims):
        grid[y] = file.readline().split('\n')[0]
    xdims = len(grid[0])

    list_lowests = find_lowest_points(grid, ydims, xdims)
    answer = sum(list_lowests) + len(list_lowests)
    print("Answer to 9.0:")
    print(answer)


if __name__ == "__main__":
    main()