def find_basin_size(point, grid, ydims, xdims, basinsize):
    y = point[0]
    x = point[1]
    north = (y - 1, x)
    south = (y + 1, x)
    west = (y, x - 1)
    east = (y, x + 1)

    if grid[y][x] != '9':
        basinsize += 1
        grid[y][x] = '9'
    if north[0] >= 0:
        if grid[north[0]][north[1]] != '9':
            basinsize = find_basin_size(north, grid, ydims, xdims, basinsize)
    if south[0] < ydims:
        if grid[south[0]][south[1]] != '9':
            basinsize = find_basin_size(south, grid, ydims, xdims, basinsize)
    if west[1] >= 0:
        if grid[west[0]][west[1]] != '9':
            basinsize = find_basin_size(west, grid, ydims, xdims, basinsize)
    if east[1] < xdims:
        if grid[east[0]][east[1]] != '9':
            basinsize = find_basin_size(east, grid, ydims, xdims, basinsize)
    return basinsize


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
                list_lowests.append((y, x))
    return list_lowests


def main():
    file = open("input.txt")
    ydims = 100
    grid = [[] for _ in range(ydims)]

    for y in range(ydims):
        grid[y] = list(file.readline().split('\n')[0])
    xdims = len(grid[y])

    list_lowests = find_lowest_points(grid, ydims, xdims)
    basin_sizes = []
    for point in list_lowests:
        basin_size = find_basin_size(point, grid.copy(), ydims, xdims, 0)
        basin_sizes.append(basin_size)
    basin_sizes.sort(reverse=True)
    answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print("Answer to 9.1:")
    print(answer)


if __name__ == "__main__":
    main()