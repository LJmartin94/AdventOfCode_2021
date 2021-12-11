def visualise(grid):
    for row in grid:
        for char in row:
            if char == 0:
                print('\033[92m' + str(char) + '\033[0m', end="")
            else:
                print(str(char), end="")
        print()
    print()


def update_point(grid, point, flashes):
    y = point[0]
    x = point[1]
    ydims = 10
    xdims = 10

    if 0 <= y < ydims and 0 <= x < xdims:
        if 1 <= grid[y][x] <= 9:
            grid[y][x] += 1
        if grid[y][x] >= 10:
            flashes = flash_point(grid, (y, x), flashes)
    return flashes


def flash_point(grid, point, flashes):
    y = point[0]
    x = point[1]

    grid[y][x] = 0
    flashes += 1

    visualise(grid)

    north = (y - 1, x)
    flashes = update_point(grid, north, flashes)
    north_east = (y - 1, x + 1)
    flashes = update_point(grid, north_east, flashes)
    east = (y, x + 1)
    flashes = update_point(grid, east, flashes)
    south_east = (y + 1, x + 1)
    flashes = update_point(grid, south_east, flashes)
    south = (y + 1, x)
    flashes = update_point(grid, south, flashes)
    south_west = (y + 1, x - 1)
    flashes = update_point(grid, south_west, flashes)
    west = (y, x - 1)
    flashes = update_point(grid, west, flashes)
    north_west = (y - 1, x - 1)
    flashes = update_point(grid, north_west, flashes)
    return flashes


def main():
    file = open("input.txt")
    flashes = 0
    ydims = 10
    grid = [[] for _ in range(ydims)]

    for y in range(ydims):
        grid[y] = list(map(int, file.readline().split('\n')[0]))

    step_total = 100

    for steps in range(step_total):
        for y in range(ydims):
            for x in range(len(grid[y])):
                if 0 <= grid[y][x] <= 9:
                    grid[y][x] += 1
        for y in range(ydims):
            for x in range(len(grid[y])):
                if grid[y][x] >= 10:
                    flashes = flash_point(grid, (y, x), flashes)

    answer = flashes
    print("Answer to 11.0:")
    print(answer)


if __name__ == "__main__":
    main()