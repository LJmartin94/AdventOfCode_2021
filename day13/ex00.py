import numpy as np
import pandas as pd


def fold_y(sheet, yfold):
    for y in range(len(sheet)):
        for x in range(len(sheet[0])):
            if y > yfold and sheet[y][x] == '#':
                sheet[yfold - (y - yfold)][x] = '#'
            x += 1
        y += 1
    y = len(sheet)
    while y > yfold:
        y -= 1
        sheet.pop(y)
    return sheet


def fold_x(sheet, xfold):
    for y in range(len(sheet)):
        for x in range(len(sheet[0])):
            if x > xfold and sheet[y][x] == '#':
                sheet[y][xfold - (x - xfold)] = '#'
            x += 1
        y += 1

    for y in range(len(sheet)):
        x = len(sheet[y])
        while x > xfold:
            x -= 1
            sheet[y].pop(x)
        y += 1
    return sheet


def main():
    lines = open("input.txt").read().split('\n')
    dots = []
    instructions = []
    breaker = 0
    for line in lines:
        if line == '':
            breaker = 1
            continue
        if breaker == 0:
            point = line.split(',')
            point = [int(point[0]), int(point[1])]
            dots.append(point)
        if breaker == 1:
            instructions.append(line)

    coords = pd.DataFrame(dots)
    dimy = coords.max(axis=0)[1] + 1
    dimx = coords.max(axis=0)[0] + 1
    sheet = [['.' for _ in range(dimx)] for _ in range(dimy)]

    for point in dots:
        sheet[point[1]][point[0]] = '#'

    for order in instructions:
        if order.find('x') != -1:
            fold_x(sheet, int(order.split("fold along x=")[1]))
        elif order.find('y') != -1:
            fold_y(sheet, int(order.split("fold along y=")[1]))

    visible_dots = 0
    for row in sheet:
        for index in row:
            if index == '#':
                visible_dots += 1
        print(row)

    answer = visible_dots
    print("Answer to 13.0:")
    print(answer)


if __name__ == "__main__":
    main()