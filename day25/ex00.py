import copy


def print_map(cucumber_map):
    for row in cucumber_map:
        string = ''.join([str(elem) for elem in row])
        print(string)
    print()
    return


def simulate_step(cm, dimy, dimx):
    moved = 0
    ccm = copy.deepcopy(cm)
    for y in range(dimy):
        for x in range(dimx):
            if ccm[y][x] == '>' and ccm[y][(x+1) % dimx] == '.':
                moved += 1
                cm[y][x] = '.'
                cm[y][(x+1) % dimx] = '>'
    ccm = copy.deepcopy(cm)
    for y in range(dimy):
        for x in range(dimx):
            if ccm[y][x] == 'v' and ccm[(y+1) % dimy][x] == '.':
                moved += 1
                cm[y][x] = '.'
                cm[(y+1) % dimy][x] = 'v'
    # print_map(cm)
    print(moved)
    return (moved, cm)

def main():
    lines = open("input.txt").read().split('\n')
    dimy = len(lines)
    dimx = len(lines[0])

    cucumber_map = [[0 for _ in range(dimx)] for _ in range(dimy)]
    y = 0
    for line in lines:
        x = 0
        for char in line:
            cucumber_map[y][x] = char
            x += 1
        y += 1

    steps = 0
    moved = 1
    while moved != 0:
        tup = simulate_step(cucumber_map, dimy, dimx)
        moved = tup[0]
        cucumber_map = tup[1]
        steps += 1

    answer = steps
    print("Answer to 25.0:")
    print(answer)


if __name__ == "__main__":
    main()