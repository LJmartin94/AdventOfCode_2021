import numpy as np
import pandas as pd


class MapPoint():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # Distance from start
        self.g = 0
        # 'Heuristic' == estimated distance to end
        self.h = 0
        # Total cost of this point (f = g + h)
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def print_map_path_open(map, path, open_path):
    print()
    for y, row in enumerate(map):
        for x, pos in enumerate(row):
            replace = 0
            for entry in path:
                if (y, x) == entry:
                    print('.', end="")
                    replace = 1
            for entry in open_path:
                if (y, x) == entry and replace == 0:
                    print(' ', end="")
                    replace = 1
            if replace == 0:
                print(map[y][x], end="")
        print()
    print()


def fetch_pos_to_check(open_list, closed_list):
    # Get 'current' position, find the lowest cost point to check
    current_point = open_list[0]
    current_index = 0

    # Below syntax is akin to: index = 0 / for item in open_list: / index += 1
    for index, item in enumerate(open_list):
        if item.f < current_point.f:
            current_point = item
            current_index = index

    # Move current index from open list to closed list
    open_list.pop(current_index)
    cp = current_point
    if cp.position not in closed_list.keys() or closed_list[cp.position] > cp.g:
        closed_list[cp.position] = cp.g
    # print(f'Checking position {current_point.position}')
    return current_point


def get_lowest_path(closed_list, end):
    path = []
    # current = closed_list[end]
    # while current is not None:  # Builds path from end to start
    #     path.append(current.position)
    #     current = current.parent
    # path = path[::-1]
    return path


def astar(map, start, end):
    # initialise starting & ending point of map
    starting_point = MapPoint(None, start)
    starting_point.g = starting_point.h = starting_point.f = 0
    prev_val = 10000

    # List of places to check & dictionary of places checked
    open_list = []
    closed_list = {}
    open_list.append(starting_point)

    # Loop until you have nothing left to check
    while len(open_list) > 0:
        # print(f'Len open: {len(open_list)} // len closed: {len(closed_list)}')
        current_point = fetch_pos_to_check(open_list, closed_list)
        # Calculate adjacents to current position
        for new_position in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            point_position = (current_point.position[0] + new_position[0], current_point.position[1] + new_position[1])
            # Check in bounds
            if not (0 <= point_position[0] < (len(map)) and
                    0 <= point_position[1] < (len(map[max(0, point_position[0])]))):
                continue
            # Check for walls
            if not str(map[point_position[0]][point_position[1]]).isdigit():
                continue
            # Create new MapPoint instance + g/h/f vals
            new_map_point = MapPoint(current_point, point_position)
            pos = new_map_point
            pos.g = current_point.g + map[pos.position[0]][pos.position[1]]
            pos.h = (abs(end[0] - pos.position[0]) + abs(end[1] - pos.position[1]))
            # pos.h = ((pos.position[0] - end[0]) ** 2) + ((pos.position[1] - end[1]) ** 2)
            pos.f = pos.g + pos.h
            # Check if position was already checked and had better cost
            if pos.position in closed_list.keys() and (closed_list[pos.position]) <= pos.g:
                continue
            # Otherwise, add it to list of positions to still be considered
            if pos not in open_list:
                open_list.append(pos)
        # Once all relevant adjacent points have been added, move this point to closed
        cp = current_point
        if cp.position not in closed_list.keys() or (closed_list[cp.position]) > cp.g:
            closed_list[cp.position] = cp
        if end in closed_list.keys():
            if closed_list[end] < prev_val:
                prev_val = closed_list[end]
                # print(get_lowest_path(closed_list, end))
                print(prev_val)

    # Potentially interesting values to return:

    # all_risk_vals = {key: (value.g) for key, value in closed_list.items()}
    lowest_end_risk_val = (closed_list[end])
    # lowest_risk_path = get_lowest_path(closed_list, end)
    return (lowest_end_risk_val)


def big_map_print(big_map):
    i = 0
    for row in big_map:
        print(row)
    print(i)
    return


def main():
    lines = open("input.txt").read().split('\n')
    dimy = len(lines)
    dimx = len(lines[0])

    map = [[0 for _ in range(dimx)] for _ in range(dimy)]
    y = 0
    for line in lines:
        x = 0
        for char in line:
            map[y][x] = int(char)
            x += 1
        y += 1

    big_map = [[0 for _ in range(dimx * 5)] for _ in range(dimy * 5)]
    for ym in range(5):
        for xm in range(5):
            for y in range(dimy):
                for x in range(dimx):
                    big_map[y + (ym * dimy)][x + (xm * dimx)] = (map[y][x] + ym + xm)
                    if big_map[y + (ym * dimy)][x + (xm * dimx)] > 9:
                        big_map[y + (ym * dimy)][x + (xm * dimx)] = big_map[y + (ym * dimy)][x + (xm * dimx)] - 9

    start = (0, 0)
    end = (((dimy * 5) - 1), ((dimx * 5) - 1))
    path = astar(big_map, start, end)

    answer = path
    print("Answer to 15.1:")
    print(answer)


if __name__ == "__main__":
    main()