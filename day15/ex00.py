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

        # Move current index from open list to closed list
        open_list.pop(current_index)
        closed_list.append(current_point)

        # Check if current position is the target destination
        if current_point == ending_point:
            path = []
            current = current_point
            while current is not None:  # Builds path from end to start
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Takes the entire path and reverses it

        # If we havent reached the ending_point yet, we travel from the current_point:
        adjacent = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get the position
            point_position = (current_point.position[0] + new_position[0], current_point.position[1] + new_position[1])
            # Make sure new point is in range, else continue with next adjacent point
            if point_position[0] > (len(map) - 1) or point_position[0] < 0 \
                    or point_position[1] > (len(map[max(0, point_position[0])]) - 1) or point_position[1] < 0:
                continue
            # Check terrain is passable if relevant - in our case it isn't;
            # so we'll just put in a placeholder that checks if the list entry is a digit.
            if not str(map[point_position[0]][point_position[1]]).isdigit():
                continue
            # Create new MapPoint instance based on this new position: (passing current_point as the parent,
            # and the point_position as this point's coordinates.
            new_map_point = MapPoint(current_point, point_position)
            # Mark the new_map_point as adjacent to the current point
            adjacent.append(new_map_point)

        # Now loop through adjacent positions
        for pos in adjacent:
            # Check if you've closed off this position before, if so continue with next pos
            for closed_pos in closed_list:
                if closed_pos == pos:
                    continue
            # Give adjacent position its g/h/f values
            pos.g = current_point.g + map[pos.position[0]][pos.position[1]]
            # Pythagorean C^2 = A^2 + B^2, for 'direct' distance to end point.
            # pos.h = ((pos.position[0] - ending_point.position[0]) ** 2) + ((pos.position[1] - ending_point.position[1]) ** 2)
            pos.h = abs(ending_point.position[0] - pos.position[0]) + abs(ending_point.position[1] - pos.position[1])
            pos.f = pos.g + pos.h
            # print("Checking pos: " + str(pos.position) + " from parent: " + str(pos.parent.position) + " G == " + str(pos.g) + " H == " + str(pos.h) + " F == " + str(pos.f))
            # Check if adjacent position is already in the open list of positions being considered ->
            # then only replace it if it has a lower cost score
            for open_pos in open_list:
                if pos == open_pos and pos.g > open_pos.g:
                    continue
            # Add adjacent pos to the open_list
            open_list.append(pos)
            # print("Open list: " + str([(entry.position, entry.f) for entry in open_list]))
            # print("Clsd list: " + str([(entry.position, entry.f) for entry in closed_list]))


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

    print()
    for y, row in enumerate(map):
        for x, pos in enumerate(row):
            replace = 0
            for entry in path:
                if (y, x) == entry:
                    print('.', end="")
                    replace = 1
            if replace == 0:
                print(map[y][x], end="")
        print()
    print()

    answer = path
    print("Answer to 15.0:")
    print(answer)


if __name__ == "__main__":
    main()