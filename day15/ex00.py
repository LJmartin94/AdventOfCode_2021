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


def astar(map, start, end):
    # initialise starting point of map
    starting_point = MapPoint(None, start)
    starting_point.g = 0
    starting_point.h = 0
    starting_point.f = 0

    # initialise ending point of map
    ending_point = MapPoint(None, end)
    ending_point.g = 0
    ending_point.h = 0
    ending_point.f = 0

    # List of places to check
    open_list = []
    # List of places checked
    closed_list = []

    # Add start to list of places to check
    open_list.append(starting_point)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get 'current' position, find the lowest cost point to check
        current_point = open_list[0]
        current_index = 0

        # Below syntax is akin to: index = 0 / for item in open_list: / index += 1
        for index, item in enumerate(open_list):
            if item.f < current_point.f:
                current_point = item
                current_index = index

    return(map)


def main():
    lines = open("test_input.txt").read().split('\n')
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

    start = (0, 0)
    end = ((dimy - 1), (dimx - 1))
    path = astar(map, start, end)

    answer = path
    print("Answer to 15.0:")
    print(answer)


if __name__ == "__main__":
    main()